declare
fun {Fact N}
	if N == 0 then 1
	else N * {Fact N-1}
	end
end

{Browse {Fact 5}}
{Browse {Fact 100}}
{Browse {Fact 10000}}
{Browse {Fact 20000}}