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
% Not yet implemented
%{Browse {IsSortedBST Root}}

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
NewRoot = {Insert Root 1}

{Browse NewRoot}
{Preorder NewRoot}