% Abs: Int, Float & Both
declare
fun {AbsInt N}
	if N < 0 then ~N else N end
end

declare
fun {AbsFloat X}
	if X < 0.0 then ~X else X end
end

declare
fun {Abs X}
	if {Value.type X} == float then 
		if X < 0.0 then ~X else X end
	else
		if X < 0 then ~X else X end
	end
end

%{Browse {AbsInt 10}}
%{Browse {AbsInt ~4}}
%{Browse {AbsFloat ~3.0}}
%{Browse {Value.type ~4.5}}

{Browse {Abs 10}}
{Browse {Abs ~4}}
{Browse {Abs ~3.0}}
{Browse {Abs ~3.96}}