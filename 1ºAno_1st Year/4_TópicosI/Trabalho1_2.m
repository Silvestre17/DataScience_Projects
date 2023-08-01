clf;
hold on;
title('Função f(x)')
set(gca,'xtick',0:1:5);
set(gca,'ytick',0:1:3);
xlim ([0.5 2.5]);
ylim ([1 2]);
ax = gca;
ax.XAxisLocation = 'origin';
ax.YAxisLocation = 'origin';
x = 1:0.01:2;
y = (3-x+(x).^(1/2)).^(1/2);
plot(x,y, 'r', 'LineWidth', 2);
txt = 'f(x)';
text(1.5, 1.75,txt, 'FontSize', 15, 'FontName', 'Times New Roman', 'Interpreter', 'LaTeX');
txt = 'x';
text(2.4,0.95,txt, 'FontSize', 15, 'FontName', 'Times New Roman', 'Interpreter', 'LaTeX');
txt = 'y';
text(0.35,1.95,txt, 'FontSize', 15,'FontName', 'Times New Roman', 'Interpreter', 'LaTeX');
y = x
plot(x,y, 'k--', 'LineWidth', 0.5);
hold off;