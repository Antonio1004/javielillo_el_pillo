listanumero=[]
def redondear():
    numero=(input("Introdue numero para redondear:"))
    for i in numero:
        listanumero.append(i)
        if listanumero!=".":
            
            print(listanumero.insert(1,.00))
        
    print(listanumero)

redondear()