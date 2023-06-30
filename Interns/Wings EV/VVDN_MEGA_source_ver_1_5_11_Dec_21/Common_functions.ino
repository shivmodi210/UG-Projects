
// This page contains main code that receives message id as an offset from base_ID, sets up bytes in message buffer 
// and calls send message function to send it.


void set_data_and_send_message(unsigned long offset)
{
  unsigned int temp;
  int j;
  byte *ptr_char;
  long l_temp;

  switch (offset) 
  {
    case 0x00:    // Message ID = 0x00FFFFF0
      // statements
      break;//----------------------------------------------------------------------------------------
      
    case 0x01:  // Message ID = 0x00FFFFF1
    {
      //temp = (int)(ch_voltage*100);// multiply  voltage by 100 and then convert that into int
      temp = (unsigned int)(ch_voltage*100);// multiply  voltage by 100 and then convert that into int
      msg_buf[0] = lowByte(temp);
      msg_buf[1] = highByte(temp);
      
      temp = (unsigned int)(ch_current*100);// multiply  current by 100 and then convert that into int
      msg_buf[2] = lowByte(temp);
      msg_buf[3] = highByte(temp);
      
      // convert calculated energy watt seconds into watt Hours by and then multiply by 10 and  convert that into int
      temp = (unsigned int)( (ch_ws/3600)*10);
      msg_buf[4] = lowByte(temp);
      msg_buf[5] = highByte(temp);
      
      temp = (unsigned int)( (ch_As/3600)*100);// convert Amp seconds into Amp Hours and then multiply by 100 
      msg_buf[6] = lowByte(temp);
      msg_buf[7] = highByte(temp);         
      break;//----------------------------------------------------------------------------------------      
    }
    case 0x02:  // Message ID = 0x00FFFFF2
    {
      temp = (unsigned int)(disch_voltage*100);// multiply  voltage by 100 and then convert that into int
      msg_buf[0] = lowByte(temp);
      msg_buf[1] = highByte(temp);
      
      temp = (unsigned int)(disch_current*100);// multiply  current by 100 and then convert that into int
      msg_buf[2] = lowByte(temp);
      msg_buf[3] = highByte(temp);
      
      // convert calculated energy watt seconds into watt Hours by and then multiply by 10 and  convert that into int
      temp = (unsigned int)( (disch_ws/3600)*10);
      msg_buf[4] = lowByte(temp);
      msg_buf[5] = highByte(temp);
      
      temp = (unsigned int)( (disch_As/3600)*100);// convert Amp seconds into Amp Hours and then multiply by 100 
      msg_buf[6] = lowByte(temp);
      msg_buf[7] = highByte(temp);
      break;//----------------------------------------------------------------------------------------
    }
  
    case 0x03:  //// Message ID = 0x00FFFFF3
    {
      temp = (unsigned int)(BMS_v*100);// multiply  BMS voltage by 100 and then convert that into int
      msg_buf[0] = lowByte(temp);
      msg_buf[1] = highByte(temp);
      
      // Note that BMS current can be max -50 amps while charging or +150 amps while discharging. 
      // So an offset of 100 amps is added. Then it is multiplied by 100 and converted to 16 bit unsigned number.
      float temp_current = BMS_I + 100;// now negative current is also positive
      temp_current = temp_current* 100;// scale it up to get 2 digits after decimal. 
      temp = (unsigned int)(temp_current);// send offsetted & scaled up value of current converted into int
      msg_buf[2] = lowByte(temp);
      msg_buf[3] = highByte(temp);
        
      // convert BMS calculated energy watt seconds into watt Hours by and then multiply by 10 and  convert that into int
      temp = (unsigned int)( (BMS_cal_e/3600)*10);
      msg_buf[4] = lowByte(temp);
      msg_buf[5] = highByte(temp);
        
      temp = (unsigned int)( (BMS_As/3600)*100);// convert BMS Amp seconds into Amp Hours and then multiply by 100 
      msg_buf[6] = lowByte(temp);
      msg_buf[7] = highByte(temp);      
      break;//----------------------------------------------------------------------------------------      
    }
          
    case 0x04:    // Message ID = 0x00FFFFF4
    {
      // cell voltages will be typically 2000 to 3800 millivolts
      temp = (unsigned int)(cellV_hi_value);// 
      msg_buf[0] = lowByte(temp);
      msg_buf[1] = highByte(temp);
      
      temp = (unsigned int)(cellV_lo_value);// 
      msg_buf[2] = lowByte(temp);
      msg_buf[3] = highByte(temp);
        
      msg_buf[4] = cell_no_highest_voltage;// location of cell no that is having highest voltage
      msg_buf[5] = cell_no_lowest_voltage;//// location of cell no that is having highest voltage
      msg_buf[6] = max_veh_range;
      
      // For Shiv modi
      vehicle_flags =0xFF;// modify this var value to change status of  vehicle flags.
      //vehicle_flags =0xFF;// modify this var value to change status of  vehicle flags.
      
      msg_buf[7] = vehicle_flags;// bits contain pedal state of throttle,brake, steering, FWD/REV/Charger  plugged
      
      break;//----------------------------------------------------------------------------------------      
    }
      
    case 0x05:  // Message ID = 0x00FFFFF5
    {
      msg_buf[0] = BMS_Soc;// 1 byte SoC 0 to 100%
      msg_buf[1] = BMS_Soh;// 1 byte SoH 0 to 100%cell voltage by 100 and then convert that into int
      msg_buf[2] = min_to_empty;// time to empty in minutes, 0 to 255 min
      msg_buf[3] = estimated_range;// distance in kms after which vehicle will come to a stop, 0 to 255 kms.
        
      msg_buf[4] = batt_max_temp;// max. tempreture of multiple sensors -0 to 255 degrees C  

      // For Shiv modi
      battery_status_flag = 0x09;// change this value to modify Battery pack status flags
      //battery_status_flag = 0xff;// change this value to modify Battery pack status flags
      
      msg_buf[5] = battery_status_flag;// battery status flags

      msg_buf[6] = min_to_full_charge;//time in minutes required to fully charge battery 0 to 255 minutes
      msg_buf[7] = battery_error_flag;// various types of error conditions are coded here
      break;//----------------------------------------------------------------------------------------
    }

    case 0x06:  // Message ID = 0x00FFFFF6
    {
      temp = (unsigned int)(vehicle_speed_kmph*100);// multiply  vehicle_speed_kmph by 100 and then convert that into int
      msg_buf[0] = lowByte(temp);
      msg_buf[1] = highByte(temp);
      
      temp = (unsigned int)(st_angle*10);// multiply raw angle in deg read from steering sensor and multiply by 10.
      msg_buf[2] = lowByte(temp);
      msg_buf[3] = highByte(temp);
      
      // ADC count of brake signal in  millivolts 
      msg_buf[4] = lowByte(brake_value);
      msg_buf[5] = highByte(brake_value);    

      //  ADC count of throttle signal in  millivolts 
      msg_buf[6] = lowByte(throttle_value);
      msg_buf[7] = highByte(throttle_value);  
  
      break;//----------------------------------------------------------------------------------------      
    }
      
    case 0x07:  //// Message ID = 0x00FFFFF7
    {     
      msg_buf[0] = lowByte(CAN_left_rpm);// left motor RPM 0 to 1000 RPM 
      msg_buf[1] = highByte(CAN_left_rpm);//     
      msg_buf[2] = CAN_left_C_temp;// left controller temperature 0 to 255 deg C
      msg_buf[3] = CAN_left_m_temp;// left motor temperature 0 to 255 deg C

      // For Shiv modi
      CAN_left_c_stat = 0x02;// change this value to modify LMC switch & status bits 
      //CAN_left_c_stat = FF;// change this value to modify LMC switch & status bits 
      
      msg_buf[4] = CAN_left_c_stat;// LMC status flags
      msg_buf[5] = CAN_left_TPS;// Left TPS i.e. speed command analog input value
      msg_buf[6] = 254;//spare byte
      msg_buf[7] = 255;//spare byte
      break;//----------------------------------------------------------------------------------------   
    }
    
    case 0x08:    // Message ID = 0x00FFFFF8
    {
      msg_buf[0] = lowByte(CAN_right_rpm);// Right motor RPM 0 to 1000 RPM 
      msg_buf[1] = highByte(CAN_right_rpm);// 
      
      msg_buf[2] = CAN_right_C_temp;// Right controller temperature 0 to 255 deg C
      msg_buf[3] = CAN_right_m_temp;// Right motor temperature 0 to 255 deg C
      
      // For Shiv modi
      CAN_right_c_stat = 0x00;// change this value to modify RMC switch & status bits 
      //CAN_right_c_stat = 0xFF;// change this value to modify RMC switch & status bits 
      
      msg_buf[4] = CAN_right_c_stat;// RMC status flags
      msg_buf[5] = CAN_right_TPS;// Right TPS i.e. speed command analog input value
      msg_buf[6] = 254;//spare byte
      msg_buf[7] = 255;//spare byte
      break;//----------------------------------------------------------------------------------------      
    }
      
    case 0x09:  // set up data in buffer for Message ID = 0x00FFFFF9
    {
      msg_buf[0]= hh;
      msg_buf[1]= mm;
      msg_buf[2]= ss;
      msg_buf[3]= dd;
      msg_buf[4]= mo;
      msg_buf[5]= lowByte(yy);
      msg_buf[6]= highByte(yy);
      msg_buf[7]= 0xFF;// spare byte
      break;//----------------------------------------------------------------------------------------      
    }
      
    case 0x0A:  // set up data in buffer for Message ID = 0x00FFFFFA
    {
      temp = (unsigned int)(alt);  
      msg_buf[0]= lowByte(temp);
      msg_buf[1]= highByte(temp);// alt set up
      temp = (unsigned int)(course_deg);  
      msg_buf[2]= lowByte(temp);
      msg_buf[3]= highByte(temp);// course set up
      msg_buf[4]= no_sats;// no of sat set up.  
      msg_buf[5]= (unsigned char)(sp_kmph);// speed set up  
      msg_buf[6]= 0xFE;
      msg_buf[7]= 0xFF;// spare byte
      break;//----------------------------------------------------------------------------------------
    }
      
    case 0x0B:  //// Message ID = 0x00FFFFFB
    {
      // set up values in message Base_ID+B:  
      // write code to convert float variable into a 4-byte array or unsigned long
      ptr_char = (byte*) (&latitude);// take a char pointer pointing to latitude float value.
      for (j =0;j<4;j++)
      {
        msg_buf[j] = *ptr_char;// byte pointed by char pointer is moved in message buffer, 
        ptr_char++;//pointer incremented    
      }
      ptr_char = (byte*) (&longitude);// take a char pointer pointing to longitude float value.
      for (j =4;j<8;j++)
      {
        msg_buf[j] = *ptr_char;// byte pointed by char pointer is moved in message buffer, 
        ptr_char++;//pointer incremented    
      }
      // all 8 bytes set in place.
      break;//----------------------------------------------------------------------------------------   
    }
   
    default:
      // statements
      break;
  }// end of switch case
  // common part for all cases
  send_message(offset);// message with offset sent.

}// end of set_data_and_send_message

void send_message( unsigned long offset)
{
  // this function assumes that 8 data bytes of data containing desired values,is stored in msg_buf.
  // Then it adds BASE_id to offset and uses that as 29-bit message ID and sends the message.
  // There is a 1 ms delay provided at the end to ensure that there is some inter-message gap.
  CAN.sendMsgBuf((BASE_id+offset),1, 8, msg_buf);// send message 
  
  delay(1);// wait 1 ms for bits to be shifted out. This intermessage delay value may be increased.
/*
  Serial.print("CAN message with id = ");//
  Serial.print(BASE_id+offset, HEX);//
  Serial.println("  sent... ");// 
*/

}// end of send_message
