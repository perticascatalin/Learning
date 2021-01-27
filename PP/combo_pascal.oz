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

{Browse {Pascal 5}}

declare
fun {TakeIth L I}
	case L of H|T then
		if I == 1 then H
		else {TakeIth T I-1} end
	else ~1 end
end

fun {Combo N K}
	{TakeIth {Pascal N+1} (K+1)}
end

{Browse {Combo 4 2}}