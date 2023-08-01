close all
figure

T = readtable('covid192020PT.xlsx')

num_dados = 30
X = (1:num_dados)';
Y = T{X, 2}

plot(X, Y, 'O')

%
num_dados = length(X)
Z = [ones(num_dados, 1) X X.^2 X.^3]

beta = inv(Z'*Z)*Z'*Y

xx = X(1):.1:X(end);
yy = beta(1)+beta(2)*xx+beta(3)*xx.^2+beta(4)*xx.^3;

hold on

plot(xx,yy)

%previsão

x_prev = 31;
y_prev = beta(1)+beta(2)*x_prev+beta(3)*x_prev.^2+beta(4)*x_prev.^3


x_dia = T{x_prev,1}
y_real = T{x_prev, 2}
