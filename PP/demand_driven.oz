declare

fun {DConsume ?Xs Acc Limit}
	if Limit > 0 then 
		local X Xr in
			Xs=X|Xr
			{DConsume Xr Acc+X Limit-1}
		end
	else Acc end
end

proc {DProduce N Xs}
	case Xs of X|Xr then
		X=N
		{DProduce N+1 Xr}
	end
end

local Xs S in
	thread {DProduce 0 Xs} end
	thread S={DConsume Xs 0 100000} end
	{Browse S}
end