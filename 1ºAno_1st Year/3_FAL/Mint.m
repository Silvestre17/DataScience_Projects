function A = Mint(n)
% matriz n x n com entradas inteiras
% de 1 até n^2
for i = 1: n
    for j = 1: n
        A(i,j)=(i-1)*n+j;
    end
end
A;
end