% Gauss & Fact
declare
fun {Gauss N}
	if N == 0 then 0
	else N + {Gauss N-1}
	end
end

{Browse {Gauss 5}}

fun {Fact N}
	if N == 0 then 1
	else N * {Fact N-1}
	end
end

{Browse {Fact 4}}

% Generic Gauss & Fact
fun {Add X Y} X + Y end
fun {Mul X Y} X * Y end

fun {GenericFact Op InitVal N}
	if N == 0 then InitVal
	else {Op N {GenericFact Op InitVal N-1}}
	end
end

fun {GaussUsingGeneric N}
	{GenericFact Add 0 N}
end

{Browse {GaussUsingGeneric 5}}

fun {FactUsingGeneric N}
	{GenericFact Mul 1 N}
end

{Browse {FactUsingGeneric 4}}