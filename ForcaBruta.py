import time

def forcaBruta(a: int, b: int) -> int:
    # Exponenciação por força bruta: multiplica 'a' por ele mesmo 'b' vezes.
    resultado = 1
    for _ in range(b):
        resultado *= a
    return resultado

def medirTempo(func, *args):
    # Mede o tempo de execução em milissegundos.
    inicio = time.time()
    func(*args)
    fim = time.time()
    return (fim - inicio) * 1000  # milissegundos

def main():
    base = 2
    expoente = 1
    arquivo = "resultados.txt"

    print("Análise Empírica — Exponenciação por Força Bruta (base 2, expoente dobrando)")
    print("Pressione CTRL+C para parar.\n")

    with open(arquivo, "w") as arq:
        arq.write("Análise Empírica — Exponenciação por Força Bruta (base 2)\n")
        arq.write("Expoente\tTempo (ms)\n")

        try:
            while True:
                tempo = medirTempo(forcaBruta, base, expoente)
                arq.write(f"{expoente}\t{tempo:.6f}\n")
                print(f"Expoente: {expoente:<10} → Tempo: {tempo:.6f} ms")
                arq.flush()
                expoente *= 2  # dobra o expoente
        except KeyboardInterrupt:
            print(f"\nExecução interrompida manualmente no expoente {expoente}.")
            print(f"Resultados salvos em '{arquivo}'.")

if __name__ == "__main__":
    main()
