%%%%%%%%%%%%%%%%%%%%%%%%%%% Descida maxima
%%%%%%%%%%%%%%%%%%%%%%%%%%% 
%%% Description:  Implements line search methods
%%% objective functions defined by f=@(x) in terms of components x(i)
%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Adjustable parameters (see section parameters)

clc
clear
close

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%% Objective Function Library
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



%===  quadratic function 
%a=10;
%f=@(x) a*x(1)^2+x(2)^2;               


%=== perturbed polinomial 
%f=@(x) (x(1)^4-12*x(1)^2-4*x(1)+x(2)^4-16*x(2)^2-5*x(2)-20*cos(x(1)-2.5)*cos(x(2)-2.9));  
f=@(x) (x(1)+4)*x(1)*(x(1)^2-100)+(x(2)^2-100)*x(2)*(x(2)-5)-.1*cos(x(1)-3.1)*cos(x(2)-1.7)


%==== Rosenbrock function 
%lambda=10; 
%f=@(x) lambda*(x(2)-x(1)^2)^2+(1-x(1))^2;   


Nvar=2;       %%% number of variables (relevant for generation of random seed
              %%% and for graphical treatment (for Nvar=1,2)   

              
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%% Finite (middle) differences computation of gradiente

dx=1e-5;   %%% step size finite differences (use with caution)

I=eye(Nvar);  %%% canonical base of R^Nvar

dfdx=@(x) (f(x+dx*I(:,1))-f(x-dx*I(:,1)))/(2*dx);  %%% derivative wrt x
              
dfdy=@(x) (f(x+dx*I(:,2))-f(x-dx*I(:,2)))/(2*dx);  %%% derivative wrt y

df=@(x) [dfdx(x) dfdy(x)]';

% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% %%%%%%%%%%%%%%%%%  Sym calculation of Gradient
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
% syms X Y 'real'   %%%%% def sym variables 
% 
% if Nvar==1
% v=X;          %%%%% vect of sym var Nvar!=1
%     elseif Nvar==2
% v=[X; Y];        %%%%% vect of sym var Nvar!=1
% end
%         
% S=f(v);           %%%%% sym expression for objective function f
% dS=jacobian(S,v); %%%%  sym calculation of gradient 
% 
% df=@(x) double(subs(dS,v,x)');  %%%% numerical gradient defined as handle
%                                 %%%% Obs: all vectors are column vect    
% 
% %df=@(x) [2*x(1); 2*x(2)]; %% manual introduction of grad in case sym 
%                              % calculation not available
%                            
                        
%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%Parameters
%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%% Stop conditions:

Nmax=100;  %%%% max number of iterations 

errodf=1e-3; %%%% threshold for 1st order condition   

%%%%%%%% Lists: 

Lista=[];    %%% of all x_k 

LNit=[];       %%% of number of iterations used

Lopt=[];     %%% optima candidates 


%%%%% Seeds: 

Nseeds=1; %%%  num of seeds; 

%%%%% range of visualization 
a=[-9; -9]; %%% a=[xmin,ymin]
b=[9; 9];     %%% b=[xmax; ymax] 
             

                               
%%%%%%%%%%%%%%%%%%%%%%%%%%                               
%%%%%%%%%%%%%%%% Line search 
%%%%%%%%%%%%%%%%%%%%%%%%%%

for i=1:Nseeds
    %x=[-1, -1]' DB;                %% manual choice of seed
    x=[4, 4]' %DC;
    %x=[-4, -4]' EB;
    %x=[-4,4]' %EC
    %x=[1,1]'

    %x=(b-a).*rand(Nvar,1)+a; %% pseudo-random choice of seed
    Lista=[Lista, x];         %% seed saved in Lista   
    dfx=df(x);                %% gradiente at x 
    N=1;                      %% set counter for number of iterations
    while norm(dfx)>errodf && N<Nmax  %%% stopping criteria 
    p=-dfx;                  %% search direction (STEEPEST DESCENT) 
    eps=.001;                %% step size
    x=x+eps*p;              %% updated iteration 
    Lista=[Lista, x];          %% save new x in Lista
    N=N+1;                         %% update numb of iterations
    dfx=df(x);                    %% new grad becomes old
    end 
    LNit=[LNit, N];          %% save numb of iterations used in corresponding list   
    Lopt=[Lopt, x];      %% save candidate to solution in corresponding list   
end  

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%% Global Minimum 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


xopt=Lopt(:,1);  %%%% 1st candidate is the 1st element in Lopt

for i=2:Nseeds
    if f(xopt)>f(Lopt(:,i)); %%%% if new candidate is better 
        xopt=Lopt(:,i);      %%%% switch   
    end
end
        

%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%% Outputs
%%%%%%%%%%%%%%%%%%%%%%%

xoptimo=xopt        %%%% Solution found  
foptimo=f(xopt)    %%%% value of objective function 
dffinal=df(xopt)    %%%% gradient at solution
Nmean=mean(LNit)   %%%% mean number of iterations used  

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%graphs  Nvar=1 and 2
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

 close all
 
 if Nvar==2 
 levelGraphs(f,a(1),b(1),a(2),b(2))   %%% draws level sets  
                                      %%% seperate M-file
 hold on
 
 graphsLineSearch(Lista,LNit,Lopt)  %%% graph treatment of iteration
                                    %%% seperate M-file
 hold off

    elseif Nvar==1

 graphsLineSearchNvar1(f,Lista,LNit,Lopt) %%% graph treatment of iteration
                                          %%% seperate M-file

 hold on

 fplot(f,[a(1),b(1)])

 hold off

 end