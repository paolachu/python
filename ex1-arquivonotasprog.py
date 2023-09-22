print ("olá")

def lerArquivo():
    #Abrindo o arquivo txt para leitura
    arquivo = open("./02-arquivonotas.txt", "r", encoding ="utf8")

    #Ler os dados do arquivo txt
    conteudoLido = arquivo.readlines()
    for linha in conteudoLido:
            valores = linha.split(";")
            qdadeItens = len(valores)

            # Verifique se há valores suficientes na linha
            if (qdadeItens > 3):
                print('Nome:', valores[0],'AV1:', valores[1],'AV2:', valores[2],'AV3:', valores[3])

    arquivo.close()
    

lerArquivo()