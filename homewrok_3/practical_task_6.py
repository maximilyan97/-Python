def init_func(word):
    """Возвращает слово с прописной первой буквой."""
    return word[0].upper() + word[1:]


words = input('Введите слова маленькимм буквами через пробел: ').split()

print(f'Перепишем каждое слово с большой буквы: {" ".join(list(map(init_func, words)))}')
