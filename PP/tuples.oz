declare
X = state(1 a 2)
Y = state(1 b 5)
Z = [X Y]
{Browse Z}
{Browse {Label X}}
{Browse {Width Y}}
{Browse X.3+Y.3}

fun {Two} 2 end

{Browse X.(1+1)}
{Browse X.{Two}}