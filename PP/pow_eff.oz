declare
fun {PowEff N M}
	if M == 0 then 1
	else
		if {IsEven M} then
			{PowEff (N * N) (M div 2)}
		else
			N * {PowEff (N * N) ((M-1) div 2)}
		end
	end
end

{Browse {PowEff 2 5}}
{Browse {PowEff 3 3}}
{Browse {PowEff 3 4}}
{Browse {PowEff 4 5}}
{Browse {PowEff 1 0}}
{Browse {PowEff 9 1}}