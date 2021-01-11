% Find an element in a list
declare
fun {Member Xs Y}
	case Xs
	of nil then false
	[] H|T then
		if H == Y then true
		else {Member T Y}
		end
	end
end

{Browse {Member [a b c] c}}
{Browse {Member [a b c] d}}