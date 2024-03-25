def points(points):
    terminaison = ["octets", "Ko", "Mo", "Go", "To", "Po", "Eo", "Zo", "Yo", "Ro", "Qo"]
    al="abcdefghijklmnopqrstuvwxyz"
    for i in range(26):
        for j in range(26):
            text = ""
            text += (al[i])
            text += (al[j])
            terminaison.append(text)
    k = 1
    while points > 1_000_000:
        points = points / 1000
        k += 1
    points = round(points / 1000, 2)
    texte = f"{points} {terminaison[k]}"
    return(texte)

print(points(6546242814984914189549816419821555))
