declare

fun {Produce N Limit}
	if N < Limit then N|{Produce N+1 Limit}
	else nil end
end

fun {Consume Xs Acc}
	case Xs of X|Xr then {Consume Xr Acc+X}
	else Acc end
end

fun {Filter Xs Op}
	case Xs of X|Xr then
		if {Op X} then X|{Filter Xr Op}
		else {Filter Xr Op} end
	else nil end
end

fun {IsOdd X}
	if X mod 2 == 0 then false
	else true end
end

declare Stream FilterResult Result
thread Stream = {Produce 0 100000} end
thread FilterResult = {Filter Stream IsOdd} end
thread Result = {Consume FilterResult 0} end
{Browse Result}