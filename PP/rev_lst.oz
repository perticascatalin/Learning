declare
fun {Reverse L R}
	case L of
		nil then R
	[] H|T then {Reverse T H|R}
	end
end

{Browse {Reverse [1 3 5 7 9] nil}}