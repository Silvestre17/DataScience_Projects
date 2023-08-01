% Cálculo a área de um triângulo
% a partir da fórmula de Héron.
% a, b, c são os comprimentos dos lados.
%
function area = areaHeron(a,b,c)
p = (a+b+c)/2;
area = sqrt(p*(p-a)*(p-b)*(p-c));
end
