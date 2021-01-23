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