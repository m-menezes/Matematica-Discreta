def calculo(indice, razao, type):
    index = 1
    result = {}
    result[index] = indice
    for n in range(2, 10):
        index += 1

        #PA
        if(type == 1):
            calculo = (indice) + ((n-1)*razao)
            print('Formula A',n,': ',indice,'+(',n-1,'-1)*',razao)
            result[index] = calculo

        #PG
        else:
            calculo = indice * (pow(razao, (n-1)))
            print('Formula A',n,': ',indice,'*(',razao,'^(',n-1,'-1))')
            result[index] = calculo

    for j in result:
        print(j,'=',result[j])

def main():
    indice = -1
    razao = -2

    calculo(indice, razao, 2)

main()
