def maiusculas(s):
    menor = ''
    for i in range(len(s)):
        if s[i] >= 'A' and s[i] <= 'Z':
            if s[i] < menor:
                menor += s[i]
            else:
                menor += s[i]
    return menor
