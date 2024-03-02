strain = 0.012;
sigma0 = 496.55072400;

%% Von Mises

syms x y % x=sigma1; y=sigma2
YF=sqrt((x^2+y^2+(x-y)^2)/2);

figure (1)
Mises = fcontour(YF,'k');
Mises.LevelList = sigma0;  % Initial Yield stress 
 
Mises.YRange = [0,800];
Mises.XRange = [0,800];

%% Hill48

r0 = 0.56;
r45 = 0.71;
r90 = 0.51;
r11 = 1;
r13 = 1;
r23 = 1;

r22 = sqrt((r90*(r0+1))/(r0*(r90+1)));
r33 = sqrt((r90*(r0+1))/(r90+r0));
r12 = sqrt((3*r90*(r0+1))/((2*r45+1)*(r90+r0)));

F = 0.5*(1/r22^2 + 1/r33^2 - 1/r11^2);
G = 0.5*(1/r11^2 + 1/r33^2 - 1/r22^2);
H = 0.5*(1/r11^2 + 1/r22^2 - 1/r33^2);

YF=(G+H)*x^2+(F+H)*y^2-2*H*x*y;

hold on
set(gca,'fontsize', 18)
Hill48 = fcontour(YF,'b');
Hill48.LevelList = sigma0^2;
Hill48.YRange = [0,800];
Hill48.XRange = [0,800];

%% Hill93
s0 = sigma0;
s90 = sigma0;

r = (r0+r90)/2;
sB = s0*sqrt((1+r)/2);

c = s0*s90*(1/s0^2 + 1/s90^2 - 1/sB^2);
p = (2*r0*(sB-s90)/(s0^2*(1+r0)) - 2*r90*sB/(s90^2*(1+r90)) + c/s0)/(1/s0 + 1/s90 - 1/sB);
q = (2*r90*(sB-s90)/(s90^2*(1+r90)) - 2*r0*sB/(s0^2*(1+r0)) + c/s90)/(1/s0 + 1/s90 - 1/sB);

YF = x^2/s0^2 - c*x*y/(s0*s90) + y^2/s90^2 + (p + q - (p*x+q*y)/sB)*(x*y/(s0*s90));

hold on
set(gca,'fontsize', 18)
Hill93 = fcontour(YF,'r');
Hill93.LevelList = 1;
Hill93.YRange = [0,800];
Hill93.XRange = [0,800];

%% Experimental
x = [496.55072400
669.712092
661.94226
637.1608680
509.140584
344.010444
0];

y = [0
331.340448
489.900564
636.6955320
711.34224
695.827704
496.550724];

hold on
plot(x,y,'--m');
legend('Von-Mises', 'Hill 48', 'Hill 93', 'Experimental');
title('Yield Loci using different criteria for 0.012 strain')
xlabel('sigmaX (MPa)')
ylabel('sigmaY (MPa)')
