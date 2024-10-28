def quick_sort(lista):
  """
  Ordena uma lista de números usando o algoritmo Quick Sort.

  Args:
    lista: Uma lista de números.

  Returns:
    A lista ordenada.
  """
  if len(lista) <= 1:
    return lista
  else:
    pivô = lista[0]
    menores = [x for x in lista[1:] if x < pivô]
    maiores = [x for x in lista[1:] if x >= pivô]
    return quick_sort(menores) + [pivô] + quick_sort(maiores)

# Exemplo de uso
lista = [5, 2, 8, 1, 9, 3, 7, 4, 6]
lista_ordenada = quick_sort(lista)
print(lista_ordenada)  # Saída: [1, 2, 3, 4, 5, 6, 7, 8, 9]
