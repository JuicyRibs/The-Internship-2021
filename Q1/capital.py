result = []
for i in range(int(input())):
    text = input().split(sep=" ")
    accro = ""
    for word in text:
        if (word[0].isupper()) :
            accro += word[0]
    result.append(accro)    

result = sorted(result, key=len, reverse=True)
for accro in result:
    print(accro)
