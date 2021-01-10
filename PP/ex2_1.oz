declare
fun {Fact N}
	if N == 0 then 1
	else N * {Fact (N-1)}
	end
end

%{Browse {Fact 5}}

% Step 0
declare
fun {Comb N K}
	{Fact N} div ({Fact K} * {Fact N-K})
end

%{Browse {Comb 6 2}}
%{Browse {Comb 10 3}}

% Step A
declare
fun {Step A B}
	if B < A then 1
	else B * {Step A B-1}
	end
end

{Browse {Step 3 6}}

%declare
%fun {Comb1 N K}