% Position of element in list 
% (element must be in list)
declare
fun {Position Xs Y}
	case Xs
	of nil then 0
	[] H|T then
		if H == Y then 1
		else 1 + {Position T Y}
		end
	end
end

{Browse {Position [a b c d] b}}