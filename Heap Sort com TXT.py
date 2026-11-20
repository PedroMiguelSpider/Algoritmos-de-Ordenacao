import random
import time
import os

def heapify(lista, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and lista[esquerda] > lista[maior]:
        maior = esquerda
    if direita < n and lista[direita] > lista[maior]:
        maior = direita
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        heapify(lista, n, maior)

def heap_sort(lista):
    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)
        
    return lista

if __name__ == "__main__":
    arquivo_aleatorio = "numeros_aleatorios.txt"
    arquivo_ordenado = "numeros_ordenados.txt"
    qtd_numeros = 100000

    if os.path.exists(arquivo_aleatorio):
        backup_nome = f"backup_{arquivo_aleatorio}"
        try:
            if os.path.exists(backup_nome):
                os.remove(backup_nome) 
            os.rename(arquivo_aleatorio, backup_nome)
            print(f"⚠️ Arquivo '{arquivo_aleatorio}' já existia. Um backup foi criado: '{backup_nome}'")
        except Exception as e:
            print(f"Erro ao tentar criar backup do arquivo existente: {e}")

    lista = [random.randint(0, 100000) for _ in range(qtd_numeros)]
    
    try:
        with open(arquivo_aleatorio, "w") as arquivo_entrada:
            for numero in lista:
                arquivo_entrada.write(f"{numero}\n")
        print(f"Arquivo '{arquivo_aleatorio}' criado com sucesso!")
    except IOError as e:
        print(f"Erro de permissão ao criar o arquivo: {e}. Verifique as permissões da pasta.")
        exit(1)

    print("\nLendo os números do arquivo...")
    lista_para_ordenar = []
    try:
        with open(arquivo_aleatorio, "r") as arquivo_entrada:
            for linha in arquivo_entrada:
                if linha.strip(): 
                    lista_para_ordenar.append(int(linha.strip()))
        print(f"Sucesso! {len(lista_para_ordenar)} números carregados na memória.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        exit(1)

    print("\nIniciando a ordenação com Heap Sort...")
    inicio = time.time()
    lista_ordenada = heap_sort(lista_para_ordenar)
    fim = time.time()
    
    print(f"⏱️ Tempo de execução do Heap Sort: {fim - inicio:.4f} segundos")

    print(f"\nSalvando números ordenados...")
    try:
        with open(arquivo_ordenado, "w") as arquivo_saida:
            for numero in lista_ordenada:
                arquivo_saida.write(f"{numero}\n")
        print(f"Arquivo '{arquivo_ordenado}' criado com sucesso!")
    except IOError as e:
        print(f"Erro de permissão ao salvar o arquivo ordenado: {e}")
