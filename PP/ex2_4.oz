% Sample binary tree implementation

declare
Root = node(left:X1 right:X2 value:6)
X1   = node(left:X3 right:X4 value:3)
X2   = node(left:X5 right:X6 value:10)
X3   = node(left:nil right:nil value:2)
X4   = node(left:nil right:nil value:4)
X5   = node(left:nil right:nil value:7)
X6   = node(left:nil right:nil value:12)

{Browse Root}

proc {Preorder X}
	if X \= nil then {Browse X.value}
		if X.left \= nil then {Preorder X.left} end
		if X.right \= nil then {Preorder X.right} end
	end
end

{Preorder Root}

% Smallest and biggest methods on a BST
fun {Smallest X}
	if X.left \= nil then {Smallest X.left}
	else X.value end
end
fun {Biggest X}
	if X.right \= nil then {Biggest X.right}
	else X.value end
end

{Browse {Smallest Root}}
{Browse {Biggest Root}}

% Additional insert function on sample binary tree
proc {Insert X N ?Y}
	case X
	of nil then Y = node(left:nil right:nil value:N)
	[] node(left:T1 right:T2 value:V) then
		if N < V then T in
			Y = node(left:T right:T2 value:V)
			{Insert T1 N T}
		else T in
			Y = node(left:T1 right:T value:V)
			{Insert T2 N T}
		end
	end
end

% To check how tree looks after insertion
%{Preorder {Insert Root 1}}

declare
NewTree = {Insert Root 1}

{Browse NewTree}
{Preorder NewTree}

% Reimplement Smallest (-Minimum) and Biggest (-Maximum) without assuming BST property (left < & right >=)

fun {Min X Y}
	if X < Y then X else Y end
end
fun {Max X Y}
	if X > Y then X else Y end
end

fun {Minimum T}
	case T
	of nil then 1000000
	[] node(left:T1 right:T2 value:V) then
		{Min V {Min {Minimum T1} {Minimum T2}}}
	end
end
fun {Maximum T}
	case T
	of nil then 0
	[] node(left:T1 right:T2 value:V) then
		{Max V {Max {Maximum T1} {Maximum T2}}}
	end
end
fun {And X Y}
	if X then
		if Y then true else false end
	else
		false
	end
end

%{Browse {Minimum Root}}
%{Browse {Maximum Root}}

% Check whether BST is sorted
fun {IsSortedBST T}
	case T
	of nil then true
	[] node(left:T1 right:T2 value:V) then
		if {And (T1 \= nil) (V < {Maximum T1})} then false
		else
			if {And (T2 \= nil) (V > {Minimum T2})} then false
			else
				true
			end
		end
	end
end

{Browse {IsSortedBST Root}}