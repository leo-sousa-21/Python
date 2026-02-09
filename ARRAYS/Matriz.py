def cria_matriz(num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input(f"Digite o valor para a posição ({i}, {j}): "))
            linha.append(valor)
        matriz.append(linha)
    return matriz
def imprime_matriz(matriz):
    for linha in matriz:
        print(linha)
num_linhas = int(input("Digite o número de linhas da matriz: "))
num_colunas = int(input("Digite o número de colunas da matriz: "))
matriz = cria_matriz(num_linhas, num_colunas)
print("Matriz criada:",imprime_matriz(matriz))
