spaf = readmatrix('main_asc_spaf.txt');
fc = readmatrix('main_asc_fc.txt');
pv = readmatrix('main_asc_pv.txt');
vt = readmatrix('main_asc_vt.txt');
sfr = importfile('main_asc_sfr.txt');

%% (i) - Cutting Force
angle = fc(1:3600,1);
Fx = fc(1:3600,2);
Fy = fc(1:3600,3);
Fz = fc(1:3600,4);

figure(1)
subplot(311)
plot(angle,Fx)
ylabel('Fx (N)','fontweight','bold')
title('Cutting Force (70k RPM, 0.25 um FPT)','fontweight','bold')
subplot(312)
plot(angle,Fy)
ylabel('Fy (N)','fontweight','bold')
subplot(313)
plot(angle,Fz)
xlabel('Angle (deg)','fontweight','bold')
ylabel('Fz (N)','fontweight','bold')
saveas(1,'F1-1.png')
%% 
% (ii) - Peak to Valley
AvgFx = sum(pv(1:10,1))/10;
AvgFy = sum(pv(1:10,2))/10;

% (iii) - Tool Deflection
AvgDx = sum(pv(1:10,3))/10;
AvgDy = sum(pv(1:10,4))/10;

%% (iv) - Surface Profile

nX = sfr(2,2);
nY = sfr(4,2);
X = sfr(3,1:nX);
Y = sfr(5,1:nY);
H = sfr(7:nY+6,1:nX);

figure(2)
surf(X, Y, H)
% title('Floor Surface (70k RPM, 0.25 um FPT)','fontweight','bold')
% xlabel('X (um)','fontweight','bold')
% ylabel('Y (um)','fontweight','bold')
% zlabel('Height (um)','fontweight','bold')
% colormap autumn
title('surface')
xlabel('X')
ylabel('Y')
zlabel('Height')
colormap default
colorbar

%% (v) - Surface Charastics
nC = find(Y==0);
nS = 128; 
center = H(nC,:);
side = H(nS,:);

figure(3)
plot(X,center)
title('Surafce Profile of Center (70k RPM, 0.25 um FPT)','fontweight','bold')
xlabel('X (um)','fontweight','bold')
ylabel('Height (um)','fontweight','bold')
saveas(3,'F1-5-center.png')

figure(4)
plot(X,side)
title('Surafce Profile of 25 um far from side (70k RPM, 0.25 um FPT)','fontweight','bold')
xlabel('X (um)','fontweight','bold')
ylabel('Height (um)','fontweight','bold')
saveas(4,'F1-5-side.png')

%% (vi) - Tool Vibrations
angle = vt(1:3600,1);
dx = vt(1:3600,2);
dy = vt(1:3600,3);

figure(5)
subplot(211)
plot(angle,dx)
title('Tool Vibrations (70k RPM, 0.25 um FPT)','fontweight','bold')
ylabel('dx (um)','fontweight','bold')

subplot(212)
plot(angle,dy)
xlabel('Angle (deg)','fontweight','bold')
ylabel('dy (um)','fontweight','bold')

saveas(5,'F1-6.png')