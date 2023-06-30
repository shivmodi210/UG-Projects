// gps variables
//float latitude,longitude,alt,course_deg,sp_kmph;
//int gps_status, dd,mo,yy,hh,mm,ss,cs,no_sats;

void init_gps_values(void)
{
  //set time = 14:28:42
  hh = 14;// 2 pm
  mm = 28;// 2 pm
  ss = 42;// 2 pm
  //set date = 25/10/2020 
  dd = 25;// 25
  mo = 10;// october
  yy = 2020;// year
  // set navigation parameters
  latitude = 22.01;
  longitude = 75.23;
  alt = 567 ;
  course_deg = 320.5;
  sp_kmph = 61;// 
  no_sats = 7;// 
  
}// end of init_gps_values


void modify_gps_values(void)
{
  //set time = 14:28:42
  hh = 14+ random(-2, +2);// 2 pm +  or - 2 hours
  mm = 28+ random(-10, +10);// 28 min  +  or - 10 minutes
  ss = 42 + random(-10, +10);// 42 seconds  +  or - 10 minutes
  //set date = 25/10/2020 
  dd = 25 + random(-3, +3 );// 25  +  or - 2 days;// 23 to 27 october
  mo = 10;// october
  yy = 2020;// year
  // set navigation parameters
  latitude = 22.01 +   random(-1.0, +1.0);// +  or - 1 degrees;
  longitude = 75.23+   random(-2.0, +2.0);// +  or - 2 degrees;
  alt = 500 + random(-100, +100);// 400 to 600 meters ;
  course_deg = 200 + random(-100, +100);// course 100 to 300 degrees.
  sp_kmph = 50 + random(-10, +10);// speed 40 to 60 kmph.
  no_sats = 7+ random(-4, +4);// no of satellites 3 to 10.  
  
}// end of modify_gps_values
