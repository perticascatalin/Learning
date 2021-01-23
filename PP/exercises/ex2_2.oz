% Reverse List
% Inefficient
declare
fun {Append L1 L2}
	case L1 of
		nil then L2
	[]	H|T then H|{Append T L2}
	end
end

fun {Reverse L1}
	case L1 of
		nil then nil
	[]	H|T then {Append {Reverse T} [H]}
	end
end

%{Browse {Reverse ['I' 'want' 2 go 'there']}}

% Efficient
declare
fun {Reverse2 L R}
	case L of
		nil then R
	[]	H|T then {Reverse2 T H|R}
	end
end

{Browse {Reverse2 ['I' 'want' 2 go 'there'] nil}}