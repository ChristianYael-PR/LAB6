def es_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generar_fibonacci_filtrado(K):
    fib = [0, 1]
    for n in range(2, 100):  # Suficientemente grande
        next_fib = fib[-1] + fib[-2]
        if next_fib > K:
            break
        if not es_primo(n):
            fib.append(next_fib)
    return fib[2:]  # Excluimos 0 y 1 iniciales si no son necesarios

def encontrar_combinacion(K, fib, start, path, resultado):
    if K == 0:
        resultado.append(path.copy())
        return
    for i in range(start, len(fib)):
        if fib[i] > K:
            continue
        if i > 0 and fib[i] == fib[i-1]:
            continue  # Evita duplicados (ej: dos '1's)
        path.append(fib[i])
        encontrar_combinacion(K - fib[i], fib, i + 1, path, resultado)
        path.pop()

def min_terminos_fibonacci(K):
    fib = generar_fibonacci_filtrado(K)
    fib = sorted(list(set(fib)), reverse=True)  # Elimina duplicados y ordena
    resultado = []
    encontrar_combinacion(K, fib, 0, [], resultado)
    if not resultado:
        return -1
    mejor_solucion = min(resultado, key=lambda x: len(x))
    return len(mejor_solucion), mejor_solucion

# Cálculo de K (ejemplo: 25/12/1995 -> K = 2715)
dia = 25
mes = 12
anio = 1995
K = dia * 100 + mes * 10 + (anio % 100)
print("K =", K)

fib_filtrado = generar_fibonacci_filtrado(K)
print("Secuencia filtrada:", fib_filtrado)

num_terminos, solucion = min_terminos_fibonacci(K)
print(f"Solución óptima: {solucion} = {sum(solucion)}")
print("Número mínimo de términos:", num_terminos)