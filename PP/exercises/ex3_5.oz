declare

fun {Eval Expr}
	case {Label Expr} of
			int then Expr.1
		[]	add then {Eval Expr.1} + {Eval Expr.2}
		[]	mul then {Eval Expr.1} * {Eval Expr.2}
	end
end

{Browse {Eval int(3)}}
{Browse {Eval add(int(1) mul(int(3) int(4)))}}