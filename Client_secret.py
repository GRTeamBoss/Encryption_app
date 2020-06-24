eng_alphabet_space = " 0123456789abcdefghijklmnopqrstuvwxyz"
rus_alphabet_space = " 0123456789абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
list_letters = []
encryption_1 = []
eng_coding = []
rus_coding = []
list_letters_result = []

def rotate(l, n):
    return l[-n:] + l[:-n]

print("Это приложение по шифрованию и пожалуйста вводите текст с маленькими буквами, в дальнейшем итог шифрования появится в новом созданном текстовом файле в той же папке где находится эта программа.")

file_name = str(input("Введите имя файла, куда выведется зашифрованный текст: "))

word = str(input("Введите ваш текст: "))

for i in range(len(word)):
    list_letters.append(word[i])

print("Сейчас вам предложат ввести шифровальный код, в дальнейшем вы можете модифицировать шифр ещё другим шифровальным кодом и т.п.")
        
encryption = str(input('Введите шифровальный код: '))

for _ in range(len(list_letters) // len(encryption) + 1):
    for i in range(len(encryption)):
        encryption_1.append(encryption[i])

alphabet_coding = str(input("Пожалуйста выберите алфавит шифровального кода (rus/eng): "))

while len(list_letters_result) < len(list_letters)+1:

    if alphabet_coding == "rus":        

        for i in range(len(list_letters)):

            if list_letters[i] in rus_alphabet_space:
                a = rus_alphabet_space.index(list_letters[i])
                b = rus_alphabet_space.index(encryption_1[i])
                list_letters_result.insert(i, rotate(rus_alphabet_space, b)[a])

            else:
                list_letters_result.insert(i, list_letters[i])
                
    elif alphabet_coding == "eng":     

        for i in range(len(list_letters)):

            if list_letters[i] in eng_alphabet_space:
                a = eng_alphabet_space.index(list_letters[i])
                b = eng_alphabet_space.index(encryption_1[i])
                list_letters_result.insert(i, rotate(eng_alphabet_space, b)[a])

            else:
                list_letters_result.insert(i, list_letters[i])
                
    else:
        None

new_file = open(f"{file_name}.txt", "a+")
new_file.write("\n----------\n")
for element in list_letters_result[:len(list_letters)]:
        new_file.write(element)
new_file.close()
print(*list_letters_result[:len(list_letters)])

print(f'Текст перенесен в созданный вами файл под именем ({file_name}.txt)')
