list1 = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

print(f'Lista sortata crescator: {sorted(list1)}')
print(f'Lista sortata descrescator: {sorted(list1, reverse = True)}')

print(f'Numerele pare din lista: {sorted(list1)[1::2]}')
print(f'Numerele impare din lista: {sorted(list1)[::2]}')

print(f'Multipli de 3: {list(filter(lambda x: not x % 3, list1))}')
