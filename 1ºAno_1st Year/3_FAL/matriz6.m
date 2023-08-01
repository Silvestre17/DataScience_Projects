n=6;
clear A;
for i=1:n
   for j=1:n
       if i<j
           A(i,j)=-1;
       elseif i>j
           A(i,j)=0;
       else
           A(i,j)=1;
       end
   end
end
A;