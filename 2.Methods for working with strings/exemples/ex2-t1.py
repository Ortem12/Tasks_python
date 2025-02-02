def analiz(text):
    char_coint = len(text)
    is_alpha = text.isalpha()

    return char_coint,is_alpha

text = input()

char_coint, is_alpha = analiz(text)

print(f"длина: {char_coint},\nалфавит: {is_alpha}")

