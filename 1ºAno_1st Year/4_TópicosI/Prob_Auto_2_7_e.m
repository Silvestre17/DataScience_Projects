clf;
hold on;
set(gca,'xtick',-8:2.0:8);
set(gca,'ytick',-4:2.0:16);
xlim ([-9 10]);
ylim ([-6 17]);
ax = gca;
ax.XAxisLocation = 'origin';
ax.YAxisLocation = 'origin';
x = -16:0.01:8.5;
y = (x.^3)./(x-1).^2;
plot(x,y, 'r', 'LineWidth', 2);
plot(0,1, 'ok');
y = (x.^3)./(x-1).^2;
plot(x,y, 'r', 'LineWidth', 2);
txt = 'x';
text(9,-1.5,txt, 'FontSize', 14);
txt = 'y';
text(-1.5,16,txt, 'FontSize', 14);
txt = 'x^3/(x-1)^2';
text(6, 12,txt, 'FontSize', 14);
% AV --> x = 0
y = -9:0.01:18;
x = y*0+1;
plot(x,y, 'b--', 'LineWidth', 1);
txt = '\leftarrow  x = 1';
text(1.1,1.5,txt);
% AO --> y = x + 2
x = -9:0.01:9;
y = x+2;
plot(x,y, 'b--', 'LineWidth', 1);
txt = '\leftarrow y = x + 2';
text(5.5,7,txt);
txt = 'y = x + 2 \rightarrow';
text(-7,-2,txt);
hold off;