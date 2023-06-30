m=2;M=5;L=4;g=10;b=1;
tspan = 0:0.1:100;

x0 = [1;0;0.1;0]; %Initial state

xf = [0;0;0;0]; %Fixed point

A = [0 1 0 0;0 -b/M -m*g/M 0;0 0 0 1;0 b/(M*L) (m+M)*g/(M*L) 0];
B = [0; 1/M; 0; -1/(M*L)];

Q = [1 0 0 0;0 1 0 0;0 0 1 0;0 0 0 1 ];
R = 1;
K = lqr(A,B,Q,R);
[t,x] = ode45(@(t,x)pendcart_Shiv(x,m,M,L,b,g,-K*(x-xf)),tspan,x0);

tiledlayout(2,2)
nexttile

plot(t,x(:,1),'r')
hold on
plot(t,repmat(xf(1),length(t),1),'b')
title('Cart position')
xlabel('t')
ylabel('l')

nexttile

plot(t,x(:,2),'r')
hold on
plot(t,repmat(xf(2),length(t),1),'b')
title('Cart speed')
xlabel('t')
ylabel('l-dot')

nexttile

plot(t,x(:,3),'r')
hold on
plot(t,repmat(xf(3),length(t),1),'b')
title('Angle')
xlabel('t')
ylabel('theta')

nexttile

plot(t,x(:,4),'r')
hold on
plot(t,repmat(xf(4),length(t),1),'b')
title('Angular speed')
xlabel('t')
ylabel('theta-dot')

disp_pendcart_Shiv(t,x,L)