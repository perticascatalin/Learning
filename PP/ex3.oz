declare
fun {MaxRec N M}
	if N == 0 then M
	else
		if M == 0 then N
		else
			1 + {MaxRec (N-1) (M-1)}
		end
	end
end

{Browse {MaxRec 5 7}}
{Browse {MaxRec 0 2}}
{Browse {MaxRec 3 0}}
{Browse {MaxRec 9 2}}