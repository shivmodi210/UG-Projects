infinite = 10^9;
lambda=1;   % Customer arrival rate
mu=1;       % Product demand rate
T = 10000;  % Timeperiod
t=0;
r=10;       % Price of product per unit
L = 5;      % Time taken to deliver order
x=2;        % amount of inventory in hand
y=20;       % amount of order
s=20;
S=50;
h=0.2;      % Holding cost per unit item per unit time
C=0;
H=0;
R=0;
c = 7;
Y = exprnd(1/lambda);
t0 = Y;
t1 = infinite;
while(1)
    if t0<t1
        H = H + (t0-t)*x*h;
        t=t0;
        D=exprnd(1/mu);
        w=min(D,x);
        R=R+w*r;
        x=x-w;
        if x<s && y==0
            y=S-x;
            t1=t+L;
        end
        Y=exprnd(1/lambda);
        t0=t+Y;
    end
    if t1<=t0
        H = H + (t1-t)*x*h;
        t=t1;
        C=C+ c*y; %C*y is a fuction c(y)
        x=x+y;
        y=0;
        t1=infinite;
    end
    if t > T && t0 ~= infinite
        t0 = infinite;
    elseif t > T && t1 == infinite && t0 == infinite
        Tp = min(t-T, 0);
        break;
    end
end
profit = R-C-H;
disp(profit);