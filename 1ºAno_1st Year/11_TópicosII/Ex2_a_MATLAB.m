close all
figure

T = readtable('covid192020PT.xlsx')

num_dados = 15
X = (1:num_dados)';
Y0 = T{X, 2}

plot(X, Y0, 'O')


%mudar escala
Y=log(Y0);

%%
num_dados = length(X)
Z = [ones(num_dados, 1) X]

beta = inv(Z'*Z)*Z'*Y

xx = X(1):.1:X(end);
yy = exp(beta(1)+beta(2)*xx);

hold on

plot(xx,yy)

%previsão

x_prev = 16;
y_prev = exp(beta(1)+beta(2)*x_prev)


x_dia = T{x_prev,1}
y_real = T{x_prev, 2}
