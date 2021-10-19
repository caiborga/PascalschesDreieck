#Berechnet Fakultät
def fakultaet(zahl)-> int:
    fakultaet = 1
    i = 1
    while (i < zahl+1):
        fakultaet = fakultaet * i
        i = i+1
    return fakultaet

#Berechnet Binominialkoeffizient
def nueberk (n,k) -> int:
    nueberk = fakultaet(n) / (fakultaet(k)*fakultaet(n-k))
    return nueberk


def get_pascals_triangle_row(row_number: int) -> list:
    pascal = [];
    if row_number == 0:
        pascal.append(1)
    else:
        for k in range(0, row_number+1):
            pascal.append(nueberk(row_number, k))
    return pascal
    
    
