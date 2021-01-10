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

%{Browse {Step 3 6}}

declare
fun {Comb1 N K}
	{Step N-K+1 N} div {Step 1 K}
end

%{Browse {Comb1 6 2}}
%{Browse {Comb1 10 3}}
%{Browse {Comb1 9 0}}

% Step B
declare
fun {Comb2 N K R A}
	if R > K then A
	else {Comb2 N K R+1 (A * (N-R+1)) div R}
	end
end

% Here we use 3rd var (R) to keep track of denominator (R) and nominator (N-R+1) and 4th var (A) to accumulate result
{Browse {Comb2 6 2 1 1}}
{Browse {Comb2 10 3 1 1}}
{Browse {Comb2 9 0 1 1}}