close all
figure

X = [1 2 3 4 5 6]';
Y = [1 1 3 5 7 9]';

plot(X, Y, 'O')

num_dados = length(X)
Z = [ones(num_dados, 1) X]

beta = inv(Z'*Z)*Z'*Y

xx = X(1):.1:X(end);
yy = beta(1)+beta(2)*xx;

hold on

plot(xx,yy)

%previsão

x_prev = 10;
y_prev = beta(1)+beta(2)*x_prev
