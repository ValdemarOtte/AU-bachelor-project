# AU Bachelor Project




##### Tekst
Som nævnt i den indledende problemstilling, så er der forskellige genstande som bliver pakket ned (kaffemaskine, bamse ovs.). Disse genstande har forskellige højde, bredde og længde.

Dette gør at hvert dimension i rygsækken får en begrænsning. 




Dermed vil the knapsack problem (KP) kunne generalisert til d-dimensional knapsack problem (d-KP)

(d-KP)
maximize sum_(j=1)^n p_j x_j
subject to sum_(j=1)^n w_ij x_j <= c_i, i = 1, 2, ..., d
x_j = {0, 1}, j = 1, 2, ..., n 

Som tidligere nævnt som ved KP, så er det antaget at p_j, w_ij og c_i > 0 (X). Moddellen tillader w_ij = 0 for et givet par i og j, såfremt at sum_(i=1)^d w_ij >= 1 overholdes forall j = 1, 2, ..., n. Dertil er det også antaget at en ændret version af (X), da det antages at alle genstande kan blive nedpakket uanset genstandes vægt i den given dimension.
w_ij <= c_i, j =1, 2, ..., n,    i=1, 2, ..., d
Tilsvarende antages det også som (X), at ingen rygsæk har sådan en stor kapacitet, at den kan indeholde alle genstande
sum_(j=1)^n w_ij >=c_i, i = 1, 2, ..., d



Hertil kommer vi til et problem. Givet følgende data
data = [
    {
        "profit": 1,
        "w_1": 1,
        "w_2": 1,
    },
    {
        "profit": 10,
        "w_1": 2,
        "w_2": 1,
    },
    {
        "profit": 15,
        "w_1": 1,
        "w_2": 2,
    },
]
og en kapacitet på c_1 = 2 og c_2 = 4

Der får vi en profit på genstand 1 og 3. Dog, ved at lade vægten blive byttet rundt for genstand 2 således at w_1 = 2 og w_2 = 1, vil det være muligt at pakke genstand 2 og 3 med en højere profit.