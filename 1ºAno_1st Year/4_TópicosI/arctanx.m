clf;
hold on;
set(gca,'xtick',-4:1:4);
set(gca,'ytick',-4:1:4);
xlim ([-5 5]);
ylim ([-5 5]);
ax = gca;
ax.XAxisLocation = 'origin';
ax.YAxisLocation = 'origin';
x = -4:0.01:4;
y = x + atan(x);
plot(x,y, 'r', 'LineWidth', 2);
y = x-pi/2;
plot(x,y, 'k--', 'LineWidth', 1);
y = x+pi/2;
plot(x,y, 'k--', 'LineWidth', 1);
txt = '\leftarrow y = x - \pi/2';
text(3,1,txt);
txt = 'y = x + \pi/2 \rightarrow';
text(-3,1,txt);
txt = 'x';
text(4.5,0.4,txt, 'FontSize', 14);
txt = 'x + arctan(x)';
text(0.2, 4.7,txt, 'FontSize', 14);
hold off;