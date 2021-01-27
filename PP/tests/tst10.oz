
declare proc {ForAll L P}
	case L of nil then skip
	[] X|L2 then {P X} {ForAll L2 P} end
end

declare L in
thread {ForAll L Browse} end

%declare L1 L2 in
%thread L=1|L1 end
%thread L1=2|3|L2 end
%thread L2=4|nil end

{ForAll [1 2 3 4] Browse}