declare
fun {Fibo N}
	case N of
		1 then 1
		[] 2 then 1
		[] M then {Fibo (M-1)} + {Fibo (M-2)}
	end
end
% Complexity: O(2^N)
% {Browse {Fibo 10}}

declare 
fun {FiboTwo N A1 A2}
	case N of 
		1 then A1
		[] 2 then A2
		[] M then {FiboTwo (M-1) A2 (A1 + A2)}
	end
end
% Complexity: O(N)
% {Browse {FiboTwo 7 1 1}}
{Browse {FiboTwo 100 1 1}}