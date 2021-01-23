declare
fun {TakeIth L P}
	case L of
	nil then nil
	[] H|T then
		if P == 1 then H
		else {TakeIth T P-1}
		end
	end
end

{Browse {TakeIth [1 3 5 7 9] 4}}