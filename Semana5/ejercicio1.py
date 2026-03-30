"""
Ejercicio 1: Dado un número entero positivo N, retornar una lista con los números desde 1 hasta N.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""

def contar_ciclo(n):
    resultado = []
    for i in range (1 , n + 1):
        resultado.append(i)
        return (resultado)
        
def contar_recursivo(n):
    if n == 1:
        return[1]
    else:
        lista = list_recur (n - 1)
        lista.append(n)
        return lista 
print(list_recur)
