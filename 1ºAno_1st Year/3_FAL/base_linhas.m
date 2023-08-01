function L = base_linhas(A)
% Base para o espaço das linhas
%
% L = base_linhas(A) devolve uma base
% para o espaço das linhas de A
% na FORMA DAS colunas de L
% Notar que L(A)=C(A')
%
L = base_colunas(A');
end