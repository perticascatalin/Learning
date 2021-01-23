% Power A^B
declare

fun {Pow A B}
	if B == 0 then 1
	else A * {Pow A B-1}
	end
end

{Browse {Pow 3 3}}
{Browse {Pow 2 5}}