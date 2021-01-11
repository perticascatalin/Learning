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

%{Preorder Root}

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

% Insert not working yet
proc {Insert X N}
	if N < X.value then
		if X.left \= nil then {Insert X.left N}
		else
			X.left = node(left:nil right:nil value:N)
		end
	else
		if X.right \= nil then {Insert X.right N}
		else
			X.right = node(left:nil right:nil value:N)
		end	
	end
end

%{Insert Root 1}
%{Preorder Root}