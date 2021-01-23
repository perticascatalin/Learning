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

% Map & Filter

% Map
fun {Map L Op}
	case L
	of nil then nil
	[] H|T then {Op H} | {Map T Op}
	end
end

fun {Minus X} ~X end
fun {Square X} X*X end
fun {AddF X} fun {$ Y} X + Y end end
Add2 = {AddF 2}
fun {MulF X} fun {$ Y} X * Y end end
Mul2 = {MulF 2}

{Browse 1 - ~3}
{Browse {Map [1 2 3] Minus}}
{Browse {Map [1 2 3] Square}}
{Browse {Map [1 2 3] Add2}}
{Browse {Map [1 2 3] Mul2}}

% Filter
fun {Filter L Op}
	case L
	of nil then nil
	[] H|T then
		if {Op H} then H | {Filter T Op}
		else {Filter T Op}
		end
	end
end

fun {Positive X}
	case {Value.type X}
	of float then X > 0.0
	[] int then X > 0
	end
end

{Browse {Positive ~1}}
{Browse {Positive 2}}
{Browse {Positive 3.2}}
{Browse {Positive ~1.5}}

{Browse {Filter [~1 2 3.2 ~1.5 4 6.4] Positive}}