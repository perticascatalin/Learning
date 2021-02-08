declare
fun {Produce N Limit}
	if N < Limit then {Pow 2 N} | {Produce N+1 Limit}
	else nil end
end

fun {Consume Xs MinP MaxP}
	case Xs of X|Xr then {Consume Xr {Min MinP X} {Max MaxP X}}
	else MinP # MaxP end
end

fun {Min X Y} if X < Y then X else Y end end
fun {Max X Y} if X > Y then X else Y end end

fun {Pow N M}
	if M == 0 then 1
	else if {IsEven M} then {Pow (N * N) (M div 2)}
	else {Pow (N * N) ((M-1) div 2)} * N end end
end

local Xs MinMax in
	thread Xs = {Produce 2 11} end
	thread MinMax = {Consume Xs 100000 0} end
	{Browse MinMax.1}
	{Browse MinMax.2}
end