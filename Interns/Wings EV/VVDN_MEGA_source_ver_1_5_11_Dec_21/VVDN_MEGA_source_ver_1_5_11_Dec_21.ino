/*
 * VVDN_MEGA_source_ver_1_5_11_Dec_21. 
 * This is as per Format version 1.5
 * 
 * This program sends 11 messages for IC + messages from 4 sources.
 * 
 * This program sends a number of CAN messages to  simulate realistic traffic (about 200 to 260 messages per second)
 * The frequency of different sources are:
 * LMC - 30 per second
 * RMC - 30 per second
 * SAS - 100 per second
 * BMS - 100 per second* 
 * GPS - 12 per second
 *  
 * 
* This program, assumes following connections:
 * Arduino D9 - CS  on CAN Bus Controller Interface Board containing 2515
 * Arduino D11 - SI or MOSI
 * Arduino D12 - SO or MISO
 * Arduino D13 - CLK or CLOCK
 * Arduino INT0 D2 - INT or Interrupt
 * 
 * 
 * Written by P W Dandekar on 06 Feb 2021.
*/

#include <mcp_can.h>
#include <SPI.h>

// the cs pin of the version after v1.1 is default to D9
// v0.9b and v1.0 is default D10
//const int SPI_CS_PIN = 9;// for UNO
const int SPI_CS_PIN = 53;// For MEGA
//Construct a MCP_CAN Object and set Chip Select to 10.
MCP_CAN CAN(SPI_CS_PIN);                            

// function prototypes
void init_gps_values(void);
void modify_gps_values(void);
void init_EM_values(void);
void init_MC_values(void);
void init_vehicle_values(void);
void send_message( unsigned long , int );

//constants
const int EXT_FRAME =1;
const int STD_FRAME =0;

// gps variables
float latitude,longitude,alt,course_deg,sp_kmph;
int gps_status, dd,mo,yy,hh,mm,ss,cs,no_sats;

// EM variables
double ch_voltage, ch_current, ch_power, ch_energywh, ch_ws, ch_As;
double disch_voltage, disch_current, disch_power, disch_energywh, disch_ws, disch_As ;// interrupts can take double but not float.

// Motor Controller variables
int CAN_left_rpm, CAN_right_rpm; //rpm    0 to 1000 rpm max.
unsigned char CAN_left_m_temp,CAN_left_C_temp;// motor & controller temperature
unsigned char CAN_right_m_temp,CAN_right_C_temp;// motor temperature if sensor installed else 0
unsigned char CAN_left_c_stat,CAN_left_s_stat;// controller and switch status
unsigned char CAN_right_c_stat,CAN_right_s_stat;// controller and switch status
unsigned char  CAN_left_ec_lsb,CAN_left_ec_msb,CAN_right_ec_lsb,CAN_right_ec_msb;// error code ls byte and ms byte
unsigned char CAN_left_TPS,CAN_right_TPS;// throttle pedal value seen by controllers between 0 to 255 indicating 0 to 5 V


// vehicle related variables
int vehicle_speed_kmph;// 0 to 255 kmph
int throttle_value, brake_value ;// store raw ADC values of value of throttle  brake here
//b_v;
//float vehicle_CG_angle_deg =0; // magnitude only.
//float vehicle_CG_angle_rad =0; // magnitude only.
int steer_dir =0;// 0 means within dead zone, -1 means left and +1 means right
int vehicle_flags = 0;
//const float st_to_tire_angle_conv_const = cg_ang_deg/ st_max;// use this to convert steering angle to vehicle CG tire angle.
long st_angle_CAN =0;
float signed_st_angle =0;// 
float st_angle =0;// 
unsigned long i_angle;//


// BMS variables
const int max_veh_range = 100;// maximum distance travelled by vehicle in this battery
int min_to_empty;// time in minutes after which battery will get discharged.
int estimated_range;// distance in kms after which vehicle will come to a stop 0 to 255 kms.
int min_to_full_charge;// time in minutes required to fully charge battery 0 to 255 minutes
double BMS_v,BMS_I, BMS_cal_p, charger_V, charger_I,BMS_cal_e, BMS_As;
int BMS_Soc,BMS_Soh;// 1 byte value
bool BMS_charging_relay_status, BMS_discharging_relay_status,battery_failure_level;
int cellV_lo_value,cellV_hi_value, cell_no_lowest_voltage,cell_no_highest_voltage;
float max_disch_current_limit;
int batt_max_temp;
//batt_min_temp ;
int battery_status_flag, battery_error_flag;// these combine multiple bits


// CAN related variables
long unsigned int BASE_id= 0x00FFFFF0; // Send only one message ID
unsigned char msg_buf[8];// buffer for all messages.
int counter =0;

// general variables
long t1, t2, t3,t4,t5,t6,t7;
int c1,c2,c3,c4,c5,c6,c7;

void setup()
{
    Serial.begin(500000);
    Serial.println("CAN BUS vehicle Traffic Simulator generating data from 5 sources - LMC, RMC,SAS,BMS,GPS..");

    //while (CAN_OK != CAN.begin(CAN_250KBPS))              // init can bus : baudrate = 250K
    while (CAN_OK != CAN.begin(CAN_1000KBPS))              //  baudrate = 500 KBPS
    {
        Serial.println("CAN BUS Module Failed to Initialized");
        Serial.println("Retrying....");
        delay(1000);        
    }
    Serial.println("CAN BUS Shield init ok!");
    Serial.println("Send different types of packets at different frequencies.");    
    // put some reasonable values in all variables
    init_gps_values();// gps values done    
    init_EM_values();// EM values done 
    init_MC_values();// MC values done 
    init_vehicle_values();// vehicle values done 
    modify_gps_values();    
    c1 = c2 = c3 = c4 = c5 = c6 = c7 = 0;// init 7 packet counters 
    t1 = t2 = t3 = t4 = t5 = t6 = t7 = millis();// SEVEN  millisecond counter variables synchronized with system timer. Only t1 used for now.
  
}// end of setup

void loop()
{   unsigned long base_id;

  // ------ task #1 Send 8 Messages sent by Control MCU with ID 0x00FFFFF1 to 0x00FFFFF8  -------------------------------------------
  if (  (millis()- t1) > 300 )  // every 300 ms, get inside and perform task.
  {  
    t1= millis();// save current millisecond counter value in  variable for next iteartion.
    unsigned long offset1;
    for ( offset1=0x01; offset1<0x0C; offset1++) // offset1 values 1 to B valid
    {
      set_data_and_send_message(offset1);// form and send message for given offset.
      counter++;// increment a counter to count number of messages sent so far.
      c4++;// IC counter incremented
    }
  
  }// end of t1 if

//-- Task #2 Send 1 packet from Steering Angle Sensor every 5 ms; desired 200 but actual may be 100 per second only.
  
  if (  (millis()- t2) > 5 )  // every 5 ms, get inside and perform task.
  {  
    t2= millis();// save current millisecond counter value in  variable for next iteartion.
    send_message( 0x114, STD_FRAME);// SAS standard packet contains 5 bytes but we are sending 8 bytes here.
    delay(1);// wait for packet to be fully transmitted
    c3++;//increment packet counter for packets sent by this source     
  }// end of t2 if
  
  
  //----------------------------- Task #3 Send packets of LMC & RMC every 30 ms (33 per second) -------------
  if (  (millis()- t3) > 30 )  // every 30 ms, get inside and perform task.
  {  
    t3= millis();// save current millisecond counter value in  variable for next iteartion.
    send_message( 0x0CF11E7B, EXT_FRAME);// LMC no. 1
    delay(1);// wait for packet to be fully transmitted
    send_message( 0x0CF11F7B, EXT_FRAME);// RMC no. 1
    delay(1);// wait for packet to be fully transmitted    
    send_message( 0x0CF11E7C, EXT_FRAME);// LMC no. 2
    delay(1);// wait for packet to be fully transmitted
    send_message( 0x0CF11F7C, EXT_FRAME);// RMC no. 2
    delay(1);// wait for packet to be fully transmitted
    c1 = c1+4;// // increment packet counter for packets sent by this source     
    //Serial.println(c1);
  }// end of t3 if
  
  //----------------------------- Task #4 Send set of 10 packets of BMS every 100 ms (110 packets per second) -------------
  if (  (millis()- t4) > 100 )  // every 100 ms, get inside and perform task.
  {  
    t4= millis();// save current millisecond counter value in  variable for next iteartion.
    // in this task we will send 1 set containing 11 packets.

    base_id = 0x18C828F4;// 
    // send 6 messages whose ID is consecutive 0x18C828F4 to 0x18CD28F4
    for (int i = 0;i<6;i++)
    { // the increment in id will be 0x000i0000 so we need to multiply i by 64K.
      send_message( (base_id+ i* (1<<16)), EXT_FRAME);// send BMS message pertaining to cell voltages 0 to 23.
      delay(1);// wait for packet to be fully transmitted.      
    }
    base_id = 0x18B428F4;// 
    // send 3 messages whose ID is consecutive 0x18B428F4 to 0x18B628F4
    for (int i = 0;i<3;i++)
    {
      send_message( (base_id+ i* (1<<16)), EXT_FRAME);// send BMS message pertaining to temperature sensors 0 to 23
      delay(1);// wait for packet to be fully transmitted.      
    }
    base_id = 0x18FE28F4;// 
    // send 2 messages whose ID is consecutive 0x18FE28F4 to 0x18FF28F4
    for (int i = 0;i<2;i++)
    {
      send_message( (base_id+ i* (1<<16)), EXT_FRAME);// send BMS message pertaining to V,I,SoC, various limits set etc.
      delay(1);// wait for packet to be fully transmitted.      
    }
    c2 = c2+11;// // increment packet counter for packets sent by this source     
    //Serial.println(c2);
  }// end of t4 if
/*  
  //----------------------------- Task #5 Send set of 3 packets of GPS data sent by R Pi every 250 ms (12 packets per second) -------------
  if (  (millis()- t5) > 250 )  // every 250 ms, get inside and perform task.
  {  
    t5= millis();// save current millisecond counter value in  variable for next iteartion.
    // in this task we will send 1 set containing 3 packets.
    base_id = 0x00FFFFF9 ;// 
    // send 3 messages whose ID is consecutive 0x00FFFFF9 to 0x00FFFFFB
    for (int i = 0;i<3;i++)
    { // the increment in id will be by 1.
      send_message( (base_id+ i), EXT_FRAME);// send GPS message pertaining to time, position etc.
      delay(1);// wait for packet to be fully transmitted.      
    }
    c4 = c4+3;// // increment packet counter for packets sent by this source     
  }// end of t5 if
*/
  
  //----------------------------- Last Task  which prints total CAN messages sent in 1 second.
  if (  (millis()- t6) > 1000 )  // every 1000 ms, print values of all packet counters and reset them
  {  
    t6= millis();// save current millisecond counter value in  variable for next iteartion.
    print_CAN_traffic();
  }// end of t6 if.

  // time var t7 is free.
  
  delay(1);// some delay to slow down the loop.    
}// end of loop


void send_message( unsigned long can_id, int frame_type)
{
  // this function assumes that 8 data bytes of data containing desired values,is stored in msg_buf.
  // Then it adds BASE_id to offset and uses that as 29-bit message ID and sends the message.
  // There is a 1 ms delay provided at the end to ensure that there is some inter-message gap.
  CAN.sendMsgBuf(can_id,frame_type, 8, msg_buf);// send message   
  //Serial.print("CAN message with id = ");//
  //Serial.print(can_id, HEX);//
  //Serial.println("  sent... ");// 
  delay(1);// wait 1 ms for bits to be shifted out. This value may be increased.

}// end of send_message

void print_CAN_traffic(void)
{
  // lmc_msg_cntr  = rmc_msg_cntr = bms_msg_cntr = sas_msg_cntr =0;// 4 message counters are reset
  Serial.print("  Packets sent in last 1 second = ");
  Serial.print("LMC & RMC = ");
  Serial.print(c1);// number of packets sent by 2 controllers together  
  Serial.print("  BMS= ");
  Serial.print(c2);// number of packets sent by BMS
  Serial.print("  SAS= ");
  Serial.print(c3);// number of packets sent by SAS
  Serial.print("  IC= ");
  Serial.print(c4);// number of packets sent by R Pi pertaining to GPS values
  
/*  
  Serial.print("  B= ");
  Serial.print(bms_msg_cntr);// print number of received from IDs pertaining to BMS  
  Serial.print("  S= ");
  Serial.print(sas_msg_cntr);// print number of received from IDs pertaining to SAS  
  Serial.print("  G= ");
  Serial.print(gps_msg_cntr);// print number of received from IDs pertaining to GPS sent by COMM 

*/
  Serial.println("");// new line
  c1 = c2 = c3 = c4 = c5 = c6 = c7 = 0;// all packet counters reset.
}// end of print_CAN_traffic
