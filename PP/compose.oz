% Functions composition

declare
fun {Compose P1 P2}
	fun {$ X} {P1 {P2 X}} end
end

fun {AddX X} fun {$ Y} X + Y end end
fun {MulX X} fun {$ Y} X * Y end end

A = {AddX 3}
B = {MulX 2}
C = {Compose B A}
{Browse {C 1}}

fun {Map L Op}
	case L
	of nil then nil
	[] H|T then {Op H} | {Map T Op}
	end
end
{Browse {Map [2 3 5 8] C}}

D = {AddX ~1}
E = {Compose D C}
{Browse {Map [2 3 5 8] E}}