
void init_EM_values(void)
{
  //Charging EM variables
  ch_voltage = 87.2;// 87.2V
  ch_current = -10.2;// 10.2 amps chrging current hence negative
  ch_power = (ch_voltage*ch_current) ;// power delivered by charger in watts
  ch_energywh = 121.3;// read energy  value from EM.arbitrary
  ch_ws = 12.34*3600;// 12.34 Watt hours multiplied by 3600 to get Watt seconds.
  ch_As = 56.78*3600;// 56.78 AH charge multiplied by 3600 to get Ampere seconds.
  
  //Discharging EM variables
  disch_voltage = 76.4;// 76.4V
  disch_current = 52.9;// 52.9 amps discharging current hence positive
  disch_power = (disch_voltage*disch_current) ;// power delivered by charger in watts
  disch_energywh = 3421.2;// read energy  value from discharging EM.
  disch_ws = 23.45 *3600;// 23.45 Watt hours multiplied by 3600 to get Watt seconds.  
  disch_As = 67.89*3600;// 67.89 AH charge multiplied by 3600 to get Ampere seconds.
  
}// end of init_EM_values
