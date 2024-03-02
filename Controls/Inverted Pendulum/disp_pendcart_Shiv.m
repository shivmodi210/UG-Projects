function disp_pendcart_Shiv(t, x, L)

pos = x(:,1);
theta = x(:,3);
%Cart
w=5;
h=1;
%Pendulum
r=0.25;
px=pos + L*sin(theta);
py=h+L*cos(theta);
%wheel
d=1;

figure()

plot([-10,20],[0,0],'w','Linewidth',2)
hold on

h1 = rectangle('Position', [pos(1)-w/2,d,w,h],'Curvature',0.1,'FaceColor',...
    [1 1 0],'EdgeColor',[0 0 0]);
h2 = plot([pos(1) px(1)],[h+d py(1)], 'w', 'LineWidth',1);
h3 = rectangle('Position',[px(1)-r py(1)-r 2*r 2*r],'Curvature',[1,1],...
    'FaceColor',[0 1 1],'EdgeColor',[0 0 0]);
h4 = rectangle('Position',[pos(1)-w/3-d/2,0,d,d],'Curvature',[1,1],'FaceColor',...
    [0.5 0 0],'EdgeColor',[0 0 0]);
h5 = rectangle('Position',[pos(1)+w/3-d/2,0,d,d],'Curvature',[1,1],'FaceColor',...
    [0.5 0 0],'EdgeColor',[0 0 0]);
xlim([-5 15]);
ylim([-10 10]);

set(gca,'Color','k','XColor','w','YColor','w')
set(gcf,'Color','k')

Button = uicontrol('Style', 'PushButton', 'String', 'End', 'Callback','delete(gcbf)');

for k = 1:length(t)
    set(h1, 'position',[pos(k)-w/2,d,w,h]);
    set(h2, 'XData', [pos(k) px(k)], 'YData',[h+d py(k)]);
    set(h3, 'position', [px(k)-r py(k)-r 2*r 2*r]);
    set(h4, 'position', [pos(k)-w/3-d/2 0 d d]);
    set(h5, 'position', [pos(k)+w/3-d/2 0 d d]);
    drawnow();
    
    if ~ishandle(Button)
        break;
    end
end