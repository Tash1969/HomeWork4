# сжатие - разжатие строки
string = 'aaaaaaaaaaaabbbbbtttttt'
zipDig = f'{string.count("a")}a{string.count("b")}b{string.count("t")}t'

print(zipDig)
unZip = ''
zip = ''
for i in zipDig:
    if i.isdigit():
        zip += i
    else:
        unZip += str(int(zip) * i)
        zip = ''
print(unZip)
