n = int(input("Ingrese numero: "))
def contar_ciclo(n):
    resultado = []
    for i in range (1 , n + 1):
        resultado.append(i)
    return (resultado)
        
def contar_recursivo(n):
    if n == 1:
        return[1]
    else:
        lista = contar_recursivo(n - 1)
        lista.append(n)
        return lista 

print(f"Resultado ciclo: {contar_ciclo(n)}")
print(f"Resultado recursivo: {contar_recursivo(n)}")

