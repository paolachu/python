print ("olá")

def lerArquivo():
    #Abrindo o arquivo txt para leitura
    arquivo = open("./02-arquivonotas.txt", "r", encoding ="utf8")

    #Ler os dados do arquivo txt
    conteudoLido = arquivo.readlines()
    for linha in conteudoLido:
            valores = linha.split(";")
            qdadeItens = len(valores)
            media = 0.0

            # Verifique se há valores suficientes na linha
            if (qdadeItens > 3):
                media = (float (valores[1]) + float (valores[2]) + float (valores[3]))/3
            else:
                media = (float (valores[1]) + float (valores[2]))/3
            print('Nome:', valores[0],'Média:{:.2f}'.format(media))
    arquivo.close()
    
    return conteudoLido



def gravarArquivo():
    #Lendo dados do arquivo
    conteudoLido = lerArquivo()

    #Abrindo arquivo para gravação
    arquivo = open("./02-arquivonotas.txt", "w", encoding="utf8")

    #Append novas linhas
    conteudoLido.append("\nJulio Amarildo;85;85")
    conteudoLido.append("\nJoelson Rodrigues;72;72")

    #Gravando as linhas adicionais.
    arquivo.writelines(conteudoLido)
    arquivo.close()

lerArquivo()
gravarArquivo()
lerArquivo()