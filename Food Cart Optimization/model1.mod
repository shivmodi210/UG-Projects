set shop;
set foodItem;

param cost{i in shop, j in foodItem} >=0;
param time{i in shop, j in foodItem} >=0;
param rating{i in shop, j in foodItem} >=0;
param satiability{i in shop, j in foodItem} > 0;

param t;
param b; 
param s;

var decision{i in shop, j in foodItem} >=0 binary;

maximize utility: sum{i in shop, j in foodItem} rating[i,j]*decision[i,j];

subject to Cost: sum{i in shop, j in foodItem} cost[i,j]*decision[i,j] <= b;
subject to Time {i in shop, j in foodItem}: time[i,j]*decision[i,j] <= t;
subject to Satiability: sum{i in shop, j in foodItem} decision[i,j]*satiability[i,j] >= s;