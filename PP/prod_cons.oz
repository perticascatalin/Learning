declare
fun {Generate N Limit}
	if N < Limit then
		N|{Generate N+1 Limit}
	else nil end
end
fun {Sum Xs A}
	case Xs
	of X|Xr then {Sum Xr A+X}
	[] nil then A
	end
end

local Xs S in
	thread Xs={Generate 0 150000} end % Producer thread
	thread S={Sum Xs 0} end
	{Browse S}
end