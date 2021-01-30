declare

fun {Filter D Xs}
	case Xs of X|Xr then
		if X mod D \= 0 then X|{Filter D Xr}
		else {Filter D Xr}
		end
	else nil end
end

fun {FilterLists Xs Ys}
	case Xs of X|Xr then {FilterLists Xr {Filter X Ys}}
	else Ys end
end

{Browse {FilterLists [2 3 5] [4 7 10 13 15 17 21]}}