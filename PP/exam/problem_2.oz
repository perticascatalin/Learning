declare

fun {Not X} if X then false else true end end
fun {Eval Expr}
	case {Label Expr}
		of boolval then Expr.1
		[] boolnot then {Not {Eval Expr.1}}
		[] boolif then
			if {Eval Expr.1} then {Eval Expr.2}
			else {Eval Expr.3}
			end
	end
end

{Browse {Eval boolval(true)}}
{Browse {Eval boolval(false)}}
{Browse {Eval boolnot(boolval(false))}}
{Browse {Eval boolif(boolval(true) boolval(true) boolval(false))}}
{Browse {Eval boolnot(boolif(boolval(false) boolval(true) boolval(false)))}}