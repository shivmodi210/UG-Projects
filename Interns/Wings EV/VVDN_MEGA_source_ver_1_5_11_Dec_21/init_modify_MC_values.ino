 /*
 Kelly 7230C controller messages
  0x0CF11E7B    LMC       RPM, Current, Voltage, Error code
  0x0CF11F7B    LMC       TPS, C & M temp, Switch status

  0x0CF11E7C    RMC       RPM, Current, Voltage, Error code
  0x0CF11F7C    RMC       TPS, C & M temp, Switch status
*/

void init_MC_values(void)
{
  //Left Motor controller values
  CAN_left_rpm = 693;// value in RPM
  CAN_left_m_temp = 40;// 56 deg C motor temp
  CAN_left_C_temp = 42;// 47 deg C controller temp
  CAN_left_c_stat = 06;//arbitrary
  CAN_left_s_stat = 07;//arbitrary 
  CAN_left_ec_lsb = 0x10;//arbitrary
  CAN_left_ec_msb = 0x11;//arbitrary
  CAN_left_TPS = 161;// left throttle signal
   
  //Right Motor controller values
  CAN_right_rpm = 689;// value in RPM
  CAN_right_m_temp = 43;// 56 deg C motor temp
  CAN_right_C_temp = 44;// 47 deg C controller temp  
  CAN_right_c_stat = 16;//arbitrary
  CAN_right_s_stat = 17;//arbitrary   
  CAN_right_ec_lsb = 0x20;//
  CAN_right_ec_msb = 0x21;//arbitrary
  CAN_right_TPS = 159;// right throttle signal
   
  
}// end of init_MC_values
