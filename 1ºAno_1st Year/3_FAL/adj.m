function B = adj(A)
% Adjunta da matriz A
[n,n]=size(A);
M = A;
B=[];
for i=1:n;
for j=1:n;
B = [B;cofator(A,i,j)];
end
end
B = reshape(B,n,n);
end

