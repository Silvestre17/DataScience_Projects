clf;
hold on;
title('1º Derivada de f(x)')
set(gca,'xtick',-10:5:10);
set(gca,'ytick',-10:5:10);
xlim ([-11 11]);
ylim ([-11 11]);
ax = gca;
ax.XAxisLocation = 'origin';
ax.YAxisLocation = 'origin';
x = -10:0.01:10;
y = (-x.^3+6*x.^2-3*x-6)./((x-2).^3);
plot(x,y, 'r', 'LineWidth', 2);
plot(2,0, 'ok');
txt = 'f´(x)';
text(-8, -2,txt, 'FontSize', 12);
txt = 'x';
text(10,-2,txt, 'FontSize', 15, 'FontName', 'Times New Roman', 'Interpreter', 'LaTeX');
txt = 'y';
text(-1.5,10,txt, 'FontSize', 15,'FontName', 'Times New Roman', 'Interpreter', 'LaTeX');
% ----- Zeros (f(x)=0) x= -0.74656, x= 1.54509, x= 5.20147 -----
plot(-0.7466,0, 'k*' );
txt = 'x= -0.74656';
text(-2,1,txt, 'FontSize', 7)
plot(5.2015,0, 'k*' );
txt = 'x= 5.2015';
text(5,0.8,txt, 'FontSize', 7)
plot(3^1/2,0, 'k*' );
txt = 'x= 1.5451';
text(0.2,-0.8,txt, 'FontSize', 6)
% ----- Assíntota Vertical (x=2) -----
y = -20:0.01:30;
x = y*0+2;
plot(x,y, 'k--', 'LineWidth', .8);
txt = '\leftarrow x = 2';
text(2.1,1.5,txt,'FontSize', 8);
hold off;