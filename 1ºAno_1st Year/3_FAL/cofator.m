function C = cofator(A,i,j)
% Matriz dos cofatores de A
%Se A for invertível, inv(A)=C’/det(A)
%C = cofator(A,i,j) retorna o cofator (i,j) de A.
if nargin==3
M = A;
M(i,:)=[];
M(:,j)=[];
C = (-1)^(i+j) * det(M);
else
[n,n]=size(A);
for i=1:n
for j=1:n
C(i,j) = cofator(A,i,j);
end
end
end
