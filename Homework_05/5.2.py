# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE

# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q



with open('text_1.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Напишите текст, необходимый для сжатия: '))
with open('text_1.txt', 'r') as file:
    my_txt = file.readline()
    my_2_txt = my_txt.split()

print(my_txt)

def encond(txt):
    en = ''
    p_char = ''
    count = 1
    if not txt:
        return ''

    for char in txt:
        if char != p_char:
            if p_char:
                en += str(count) + p_char
            count = 1
            p_char = char
        else:
            count += 1
    else:
        en += str(count) + p_char
        return en


my_2_txt = encond(my_txt)

with open('text_2.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{my_2_txt}')
print(my_2_txt)


