% Zip and UnZip pairs and lists
declare
fun {Zip P}
	case P
	of nil # nil then nil
	[] (H1|T1) # (H2|T2) then (H1 # H2)|{Zip (T1 # T2)}
	end
end

fun {UnZip L}
	case L
	of nil then nil # nil
	[] H|T then (H.1|{UnZip T}.1) # (H.2|{UnZip T}.2)
	end
end

{Browse {Zip [a b c]#[1 2 3]}}
{Browse {UnZip [a#1 b#2 c#3]}}