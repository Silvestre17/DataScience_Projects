function nivelGraficos(f,a,b,c,d)

%%%%%%%%%%%%% inputs: objective function as handle f=@(x) in terms of x(1) 
%%%%%%%%%%%%%%%%%%%%% and x(2), where x is in R^2
%%%%%%%%%%%%% output: level sets of f in [a,b]*[c,d], 
%%%%%%%%%%%%%%%%%%% and -grad in the same interval

h=1e-1;   %%% size of subintervals
x=a:h:b;  %%% partition of [a,b]
y=c:h:d;  %%% partition of [c,d] 


[X,Y]=meshgrid(x,y); %%% generates grid of X's and  Y's. 

for i=1:length(y)
    for j=1:length(x)
        v=[X(i,j),Y(i,j)];
        Z(i,j)=f(v);   %%%% matrix w/ function values 
    end
end


%[d1,d2]=gradient(Z, h);  %%% numerical gradient


meshc(X,Y,Z)            %%% function graph

figure

contour(X,Y,Z,'ShowText','on')          %%% level sets   

%hold on

%quiver(X,Y,-d1,-d2)      %%% representation of  -gradient 



