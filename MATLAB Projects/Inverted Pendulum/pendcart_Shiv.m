function dx = pendcart_Shiv(x,m,M,L,b,g,u)

dx(1,1) = x(2); % x = [l l_dot theta theta_dot]
dx(2,1) = (u + m*L*sin(x(3))*x(4)^2 - m*g*sin(x(3))*cos(x(3))-b*x(2))/(M+m*sin(x(3))^2);
dx(3,1) = x(4);
dx(4,1) = (u*cos(x(3)) - (M+m)*g*sin(x(3)) + m*L*sin(x(3))*cos(x(3))*x(4)^2 - b*x(2)*cos(x(3)))/(m*L*cos(x(3))^2 - (M+m)*L);
end