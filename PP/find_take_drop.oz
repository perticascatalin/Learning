declare
fun {Find L X}
	case L of
		nil then false
	[]	H|T then
		if H == X then true
		else {Find T X}
		end 
	end
end

fun {Take L K}
	if K == 0 then nil
	else case L of H|T then H|{Take T K-1} else nil end end
end

fun {Drop L K}
	if K == 0 then L
	else case L of H|T then {Drop T K-1} else nil end end
end

{Browse {Find [a b c d f] e}}
{Browse {Find [a b c d f] f}}
{Browse {Find [a b c d f] c}}

{Browse {Take [a b c d e f] 3}}
{Browse {Take [a b c d e f] 2}}
{Browse {Take [a b c d e f] 0}}
{Browse {Take [a b c d e f] 7}}

{Browse {Drop [a b c d e f] 3}}
{Browse {Drop [a b c d e f] 7}}
{Browse {Drop [a b c d e f] 1}}