declare PascalRow AddLists ShiftLeft ShiftRight

fun lazy {PascalRow Row}
	Row|{PascalRow {AddLists {ShiftLeft Row} {ShiftRight Row}}}
end

fun {AddLists L1 L2}
	case L1 of H1|T1 then
		case L2 of H2|T2 then (H1+H2)|{AddLists T1 T2}
		else nil end
	else nil end
end

fun {ShiftLeft L}
	case L of H|T then H|{ShiftLeft T}
	else [0] end
end

fun {ShiftRight L} 0|L end

declare
L = {PascalRow [1]}
{Browse L}
{Browse L.1}
{Browse L.2.1}
{Browse L.2.2.1}
{Browse L.2.2.2.1}