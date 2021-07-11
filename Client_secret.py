#!usr/bin/env python3
# -*- coding: utf-8 -*-
import random


class Encrypt:


    def docs():
        info = \
        """
        This app for encrypt your text
        Please post in this app word with small symbol
        result will be output in *.txt file where located this file
        """
        return info


    def encrypt(word, code, alphabet):
        list_letters = []
        list_letters_result = []
        code_1 = []
        code_2 = []
        eng_alphabet_space = " 0123456789abcdefghijklmnopqrstuvwxyz"
        rus_alphabet_space = " 0123456789абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        
        def rotate(l, n):
            return list(l[-n:] + l[:-n])

        def generate(arg, arg2):
            gen = list()
            if arg == 'eng':
                for i in range(0, 100):
                    num = random.randint(0, len(arg2)-1)
                    gen.append(arg2[num])
            if arg == 'rus':
                for i in range(0, 100):
                    num = random.randint(0, len(arg2)-1)
                    gen.append(arg2[num])
            return gen

        for i in word:
            list_letters.append(i)
        
        if alphabet == 'rus':
            generic = list(generate('rus', rus_alphabet_space))
            count = 0
            for n in code:
                if n in generic:
                    code_1.append('')
                    code_1[count] = rotate(rus_alphabet_space, generic.index(n))[0]
                    count += 1
                else:
                    code_1.append('')
                    code_1[count] = generic[code.index(n)]
                    count += 1
            code_1 = ''.join(code_1)
        
        if alphabet == 'eng':
            generic = list(generate('eng', eng_alphabet_space))
            count = 0
            for n in code:
                if n in generic:
                    code_1.append('')
                    code_1[count] = rotate(eng_alphabet_space, generic.index(n))[0]
                    count += 1
                else:
                    code_1.append('')
                    code_1[count] = generic[code.index(n)]
                    count += 1
            code_1 = ''.join(code_1)

        for n in range(len(list_letters) // len(code_1) + 1):
            for i in code_1:
                code_2.append(i)

        while len(list_letters_result) < len(list_letters)+1:

            if alphabet == "rus":        
                for i in list_letters:

                    if i in rus_alphabet_space:
                        a = rus_alphabet_space.index(i)
                        b = rus_alphabet_space.index(code_2[list_letters.index(i)])
                        list_letters_result.insert(list_letters.index(i), rotate(rus_alphabet_space, b)[a])

                    else:
                        list_letters_result.insert(list_letters.index(i), i)
                        
            if alphabet == "eng":     

                for i in list_letters:

                    if i in eng_alphabet_space:
                        a = eng_alphabet_space.index(i)
                        b = eng_alphabet_space.index(code_2[list_letters.index(i)])
                        list_letters_result.insert(list_letters.index(i), rotate(eng_alphabet_space, b)[a])

                    else:
                        list_letters_result.insert(list_letters.index(i), i)
        result = [i for i in list_letters_result[:len(list_letters)]]
        result = ''.join(result)
        return result

print(Encrypt.encrypt('Hello World other people', 'hidufgnkhi2h13kjnlvx', 'eng'))