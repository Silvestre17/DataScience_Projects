function C = base_colunas(A)
% Base para o espaço das colunas de A.
%
% C = base_colunas(A) devolve uma base
% para o espaço das colunas de A,
% escolhendo a coluna de cada pivot.
%
[S, pivotcoluna] = rref(A);
C = A(:, pivotcoluna);
end
