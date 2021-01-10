declare
fun {Sieve L}
	case L
		of nil then nil
		[] H|T then H|{Sieve {Filter T H}}
	end
end

fun {Filter L H}
	case L
		of nil then nil
		[] A|As then 
			if (A mod H)==0 then {Filter As H}
			else A|{Filter As H}
			end
	end
end

fun {Take L N}
	if N < 1 then nil
	else 
		case L
			of nil then nil
			[] X|Xs then X|{Take Xs (N-1)}
		end
	end
end

fun lazy {Prime} {Sieve {Gen 2}} end
fun lazy {Gen N} N|{Gen N+1} end

{Browse {Prime}}

fun {GetAfter N}
	{Take {Prime} N+1}
end
{Browse {GetAfter 10}}