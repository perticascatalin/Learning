% Pow: N^M
declare
fun {Pow N M}
	if M == 0 then
		1
	else
		N * {Pow N (M-1)}
	end
end

{Browse {Pow 2 4}}