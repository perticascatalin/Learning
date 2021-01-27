declare PascalRow OpList ShiftLeft ShiftRight Add Xor

fun lazy {GenericPascalRow Op Row}
	Row|{GenericPascalRow Op {OpList Op  {ShiftLeft Row} {ShiftRight Row}}}
end

fun {Add X Y} X+Y end
fun {Xor X Y} if X == Y then 0 else 1 end end

fun {OpList Op L1 L2}
	case L1 of H1|T1 then
		case L2 of H2|T2 then {Op H1 H2}|{OpList Op T1 T2}
		else nil end
	else nil end
end

fun {ShiftLeft L}
	case L of H|T then H|{ShiftLeft T}
	else [0] end
end

fun {ShiftRight L} 0|L end

declare
L = {GenericPascalRow Xor [1]}
{Browse L}
{Browse L.1}
{Browse L.2.1}
{Browse L.2.2.1}
{Browse L.2.2.2.1}
{Browse L.2.2.2.2.1}