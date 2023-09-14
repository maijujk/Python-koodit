def rivi_oikein(sudoku: list, rivi: int):
    luvut = []
    for luku in sudoku[rivi]:
        if luku > 0 and luku in luvut:
            return False
        luvut.append(luku)
    return True
 
def sarake_oikein(sudoku: list, sarake: int):
    luvut = []
    for rivi in sudoku:
        luku = rivi[sarake]
        if luku > 0 and luku in luvut:
            return False
        luvut.append(luku)
    return True 
 
def nelio_oikein(sudoku: list, rivi_nro: int, sarake_nro: int):
    luvut = []
    for r in range(rivi_nro, rivi_nro + 3):
        for s in range(sarake_nro, sarake_nro + 3):
            luku = sudoku[r][s]
            if luku > 0 and luku in luvut:
                return False
            luvut.append(luku)
    return True

def sudoku_oikein(sudoku: list):
    for rivi in range(0,9):
        if not rivi_oikein(sudoku, rivi):
            return False
 
    for sarake in range(0,9):
        if not sarake_oikein(sudoku, sarake):
            return False
 
    for rivi in range(0,9,3):
        for sarake in range(0,9,3):
            if not nelio_oikein(sudoku, rivi, sarake):
                return False
 
    return True

a = ["x","u","a"]      
a = a + ["e", "b", "c"]
a.sort()               
print(a[2])  
            
if __name__ == "__main__":
 sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
 ]

 print(sudoku_oikein(sudoku1))

 sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
 ]

 print(sudoku_oikein(sudoku2))