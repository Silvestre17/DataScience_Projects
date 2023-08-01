clf;
hold on;
title('2º Derivada de f(x)')
set(gca,'xtick',-10:5:10);
set(gca,'ytick',-10:5:10);
xlim ([-11 11]);
ylim ([-11 11]);
ax = gca;
ax.XAxisLocation = 'origin';
ax.YAxisLocation = 'origin';
x = -10:0.01:10;
y = (-18*x +24)./((x-2).^4);
plot(x,y, 'r', 'LineWidth', 2);
plot(2,0, 'ok');
txt = 'f´´(x)';
text(-8, 2,txt, 'FontSize', 12);
txt = 'x';
text(10,-2,txt, 'FontSize', 15, 'FontName', 'Times New Roman', 'Interpreter', 'LaTeX');
txt = 'y';
text(20,-1.5,txt, 'FontSize', 15,'FontName', 'Times New Roman', 'Interpreter', 'LaTeX');
% ----- Zeros (f(x)=0) -----
plot(4/3,0, 'k*' );
txt = 'x= 4/3';
text(-2.3,-0.8,txt, 'FontSize', 7)
% ----- Assíntota Vertical (x=2) -----
y = -20:0.01:30;
x = y*0+2;
plot(x,y, 'k--', 'LineWidth', .8);
txt = '\leftarrow x = 2';
text(2.1,1.5,txt,'FontSize', 8);
hold off;