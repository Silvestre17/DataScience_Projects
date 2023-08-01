% Programa que lê dois números, faz a divisão
% de um pelo outro, detetando se o denominador é zero
%
num1 = input ('Indique o 1º número: ');
num2 = input ('Indique o 2º número: ');
if (num2==0)
num3 = NaN;
disp('O divisor é zero');
else;
num3 = num1/num2;
end
disp(num3);

