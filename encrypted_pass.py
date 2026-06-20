alphabet = "abcdefghijklmnopqrstuvwxyz"

# Алфавит со сдвигом на 3 символа
cipher_word = alphabet[3:] + alphabet[:3]

secret_word = input("please enter secret word: ")

# Сразу переводим всё слово в нижний регистр (безопасно и без лишних if)
secret_word = secret_word.lower()

encrypted_word = ""
index = 0

while index < len(secret_word):
    current_char = secret_word[index]
    # Ищем индекс текущей буквы в обычном алфавите
    char_index = alphabet.find(current_char)
    
    if char_index != -1:
        # Если буква найдена, берем замену из зашифрованного алфавита
        encrypted_word = encrypted_word + cipher_word[char_index]
    else:
        # Если это пробел или символ, оставляем как есть
        encrypted_word = encrypted_word + current_char
    index += 1

print("Результат шифрования: " + encrypted_word)
