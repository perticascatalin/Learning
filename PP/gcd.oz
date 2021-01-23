declare
fun {GCD A B}
	if A == B then A
	else
		if A > B then {GCD (A-B) B}
		else {GCD B A}
		end
	end
end

{Browse {GCD 12 18}}