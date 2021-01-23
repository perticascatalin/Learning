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

{Browse {Find [a b c d f] e}}
{Browse {Find [a b c d f] f}}
{Browse {Find [a b c d f] c}}