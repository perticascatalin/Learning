declare Pascal AddLists ShiftLeft ShiftRight

fun {AddLists L1 L2}
	case L1 of H1|T1 then 
		case L2 of H2|T2 then (H1+H2)|{AddLists T1 T2}
		else nil end
	else nil end
end

fun {ShiftLeft L}
	case L of
		nil then [0]
		[] H|T then H|{ShiftLeft T}
	end
end

fun {ShiftRight L}
	0|L
end

fun {Pascal N}
	if N == 1 then [1]
	else L in
		L = {Pascal N-1}
		{AddLists {ShiftLeft L} {ShiftRight L}}
	end
end

%{Browse {Pascal 2}}
%{Browse {ShiftLeft [1 3 3 1]}}
%{Browse {ShiftRight [1 3 3 1]}}

{Browse {AddLists [1 2 3] [2 4 6]}}
{Browse {Pascal 5}}