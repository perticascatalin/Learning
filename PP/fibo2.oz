% Fibonacci with accumulator again
declare
fun {Fibo N A1 A2}
	case N of
		1 then A1
	[]	2 then A2
	[]	M then {Fibo (M-1) A2 (A1+A2)}
	end
end

{Browse {Fibo 5 1 1}}