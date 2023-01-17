# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# in
# Enter the name of the file with the text:
# 'text_words.text'
# Enter the file name to record:
# 'text_code_words.text'
# Enter the name of the file to decode:
# 'text_code_words.text'
# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
# out in file
# 'text_words.text'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ
# 'text_code_words.text'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q



def coding(text):
    count = 1
    result = ''
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            count += 1
        else:
            result = result + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text)-2] != text[-1]):
        result = result + str(count) + text[-1]
    return result


def decoding(text):
    number = ''
    result = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            number += text[i]
        else:
            result = result + text[i] * int(number)
            number = ''
    return result

r = input("Введите текст для кодировки: ")

with open('text_code_words.txt', 'w') as file:
    decoded_string = coding(r)
    file.write(decoded_string)

with open('text_words.txt', 'w') as file:
    encoded_string = decoding(coding(r))
    file.write(encoded_string)

print(f"Текст после кодировки: {coding(r)}")
print(f"Текст после дешифровки: {decoding(coding(r))}")