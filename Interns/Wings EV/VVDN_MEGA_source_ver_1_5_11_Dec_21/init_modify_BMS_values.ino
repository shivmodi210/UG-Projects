
void init_BMS_values(void)
{
  BMS_v = 76.7;// 76.7V
  BMS_I = 53.3;// 53.3 amps
  BMS_cal_p = BMS_v * BMS_I;//
  BMS_cal_e = 44.55 *3600;// 44.55 Watt hours multiplied by 3600 to get Watt seconds.  
  // Energy delivered by battery to mootor in watt seconds - divide by 1000 to get watt hours
                // initial value 0 when simulation started.
  BMS_As = 43.21*3600;// 43.21 AH charge multiplied by 3600 to get Ampere seconds.
  cellV_lo_value = 2401;// 2.401V
  cellV_hi_value = 3599;// 3.599V
  cell_no_lowest_voltage = 22;// 22 nos cell has lowest voltage
  cell_no_highest_voltage = 10;// cell no 10 has highest voltage
  //max_veh_range = 100;// maximum range given temporarily. This could be later reduced to 70 or 80 kms.
  BMS_Soc = 68;// 68% charge remaining in battery
  BMS_Soh = 100;// battery is new and its capacity is intact as rated.
  min_to_empty = 45;// 45 minutes the vehicle will run 
  estimated_range = 43;// 43 kms it run before becoming empty
  batt_max_temp = 48;// max temperature recorded inside battery 
  battery_status_flag = 0x33;// arbitrary value
  min_to_full_charge = 240;// 4 hours needed for full charge
  battery_error_flag = 0x47;// arbitrary value
  
}// end of init_BMS_values
