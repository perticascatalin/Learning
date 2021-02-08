declare

fun {FstPosition Xs Y}
	case Xs of X|Xr then
		if X == Y then 1
		else
			local P in
				P = {FstPosition Xr Y}
				if P \= 0 then P+1
				else 0 end end
		end
	else 0 end
end

fun {SndPosition Xs Y}
	case Xs of X|Xr then
		if X == Y then 
			local P in
				P = {FstPosition Xr Y}
				if P \= 0 then P+1
				else 0 end end
		else
			local P in
				P = {SndPosition Xr Y}
				if P \= 0 then P+1
				else 0 end end
		end
	else 0 end
end

{Browse {SndPosition [4 3 4 1] 4}}
{Browse {SndPosition [4 3 2 1] 4}}
{Browse {SndPosition [2 3 5 1] 4}}