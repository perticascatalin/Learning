declare

fun {IthPos Xs Y I}
	case Xs
		of X|Xr then
			if X == Y then
				if I == 1 then 1
				else if {IthPos Xr Y I-1} \= 0 then {IthPos Xr Y I-1} + 1
				else 0 end end
			else if {IthPos Xr Y I} \= 0 then {IthPos Xr Y I} + 1
			else 0 end end
		[] nil then 0 end
end

fun {SndPos Xs Y} {IthPos Xs Y 2} end

{Browse {SndPos [2 4 3 4] 4}}
{Browse {SndPos [2 4 3 1] 4}}
{Browse {SndPos [2 1 3 5] 4}}