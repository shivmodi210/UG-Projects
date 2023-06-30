

void init_vehicle_values(void)
{
  vehicle_speed_kmph = 56;// 56 kmph
  throttle_value = 3127;// 3127 millivolts
  brake_value = 290;// minimum brake value
  vehicle_flags = 0x07;// arbitrary
  st_angle_CAN = 262;// 26.2 deg steering angle , tire angle diffferent.
  steer_dir = 1;// right turn
  signed_st_angle = 26.2;//
  st_angle = 26.2;//magnitude only 
  
  //b_v = 78;// battery voltage 78V
  //vehicle_CG_angle_deg = 57.3;//
  
}// end of init_vehicle_values
