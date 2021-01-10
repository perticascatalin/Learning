declare
fun {Minus X}
	~X
end

{Browse {Minus 15}}

declare
fun {Max X Y}
	if X > Y then X else Y end
end

declare
X = {Max 22 18}
Y = {Max X 43}

{Browse Y}