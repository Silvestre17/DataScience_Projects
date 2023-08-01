clf;
hold on;
title('Função f(x)')
set(gca,'xtick',-10:10:20);
set(gca,'ytick',-20:10:10);
xlim ([-11 21]);
ylim ([-21 11]);
ax = gca;
ax.XAxisLocation = 'origin';
ax.YAxisLocation = 'origin';
x = -10:0.01:20;
y = (3*x-x.^3)./(x-2).^2;
plot(x,y, 'r', 'LineWidth', 2);
plot(2,0, 'ok');
txt = 'f(x)';
text(-5, 5,txt, 'FontSize', 12);
txt = 'x';
text(-2,10,txt, 'FontSize', 15, 'FontName', 'Times New Roman', 'Interpreter', 'LaTeX');
txt = 'y';
text(20,-1.5,txt, 'FontSize', 15,'FontName', 'Times New Roman', 'Interpreter', 'LaTeX');
% ----- Zeros (f(x)=0) -----
plot(-3^1/2,0, 'k*' );
txt = 'x = -√3';
text(-2.3,-0.8,txt, 'FontSize', 7)
plot(0,0, 'k*' );
txt = 'x = 0';
text(-1.1,0.8,txt, 'FontSize', 7)
plot(3^1/2,0, 'k*' );
txt = 'x = √3';
text(0.2,-0.8,txt, 'FontSize', 7)
% ----- Assíntota Vertical (x=2) -----
y = -20:0.01:30;
x = y*0+2;
plot(x,y, 'k--', 'LineWidth', .8);
txt = '\leftarrow x = 2';
text(2.1,1.5,txt,'FontSize', 11);
% ----- Assíntota Oblíqua -----
x = -10:0.01:20;
y = -x-4;
plot(x,y, 'k--', 'LineWidth', .8);
txt = '\leftarrow y = - x - 4';
text(10,-13,txt);
txt = 'y = - x - 4 \rightarrow';
text(-10.5,2.5,txt);
hold off;