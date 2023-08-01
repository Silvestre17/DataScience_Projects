% Cálculo a área de um triângulo
% a partir dos vértices
%
function at = areaTri(a,b,c,d,e,f)
x= norm([a-c;b-d]);
y= norm([a-e;b-f]);
z= norm([c-e;d-f]);
at= areaHeron(x,y,z);
end

