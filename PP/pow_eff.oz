declare
fun {PowEff N M A}
	if M == 0 then 1
	else
		if M == 1 then A
		else
			if {IsEven M} then
				{PowEff N (M div 2) (A * A)}
			else
				{PowEff N ((M-1) div 2) (N * A * A)}
			end
		end
	end
end
{Browse {PowEff 4 5 4}}