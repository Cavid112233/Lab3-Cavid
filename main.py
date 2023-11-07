import numpy as np
def bas_diagonal_ortalama_hesapla(A):
    n = len(A)
    
   
    toplam = 0
    
    
    for i in range(n):
        toplam += A[i][i]
    ortalama = toplam / n
    
    return ortalama
A = np.array[[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

ortalama = bas_diagonal_ortalama_hesapla(A)
print("Baş diaqonalin ortalaması:", ortalama)
