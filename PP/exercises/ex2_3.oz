% Lazy Primes Sieve

declare

% Sieve (lazy): finds the prime numbers by filtering the tail using the head
fun lazy {Sieve L}
	case L
		of nil then nil
		[] H|T then H|{Sieve {Filter T H}}
	end
end

% Filter (lazy): filters a list L based on divisibility with H
fun lazy {Filter L H}
	case L
		of nil then nil
		[] A|As then 
			if (A mod H)==0 then {Filter As H}
			else A|{Filter As H}
			end
	end
end

% Take: helper function to test retrieving first N prime numbers
fun {Take L N}
	if N < 1 then nil
	else 
		case L
			of nil then nil
			[] X|Xs then X|{Take Xs (N-1)}
		end
	end
end

% TakeFirstGreater: checks whether head > N, otherwise repeats procedure in tail
fun {TakeFirstGreater L N}
	case L
		of nil then ~1
		[] X|Xs then
			if X > N then X
			else {TakeFirstGreater Xs N}
			end
	end
end

fun {GetAfter N} 
	{TakeFirstGreater {Prime} N}
end

fun {Prime} {Sieve {Gen 2}} end
fun lazy {Gen N} N|{Gen N+1} end

{Browse {Prime}}
{Browse {Take {Prime} 10}}
{Browse {GetAfter 10}}
{Browse {GetAfter 27}}