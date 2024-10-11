def Palavras() -> None:
    palavras = []
    dicas = []
    for i in range(3):
        palavra = input("Digite a palavra: ")
        dica = input("Digite a dica: ")
        palavras.append(palavra)
        dicas.append(dica)
    return palavras, dicas

def JogoForça (palavras, dicas) -> None: 
    