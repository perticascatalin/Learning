declare
fun lazy {F1 X} X*X end
fun lazy {Ints N} N|{Ints N+1} end
A = {F1 5}
{Browse A}
B = {Ints 3}
C = 2 * A
{Browse A}
{Browse B}
case B of X|Y|Z|_ then {Browse X+Y+Z} end
