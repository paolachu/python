print ("olá")

def lerArquivo():
    #Abrindo o arquivo txt para leitura
    arquivo = open("./02-arquivonotas.txt", "r", encoding ="utf8")

    #Ler os dados do arquivo txt
    conteudoLido = arquivo.readlines()
    for linha in conteudoLido:
            valores = linha.split(";")
            qdadeItens = len(valores)
            menor = 110.0
            maior = 0.0
            for nota in valores:
                nota = nota.replace("\n","")
                if ((nota.isdigit()) and (float(nota) > maior)):
                    maior = float(nota)
                if ((nota.isdigit()) and (float(nota) < menor)):
                    menor = float(nota)
            print('Nome:', valores[0],"\n         Maior Nota: " , maior,"\n         Menor Nota: " , menor)

    arquivo.close()

lerArquivo()