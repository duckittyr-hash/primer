meme_dict = {
    "cringe": "Algo raro ",
    "lol":"Respuesta a algo gracioso",
    "creepy": "Algo aterrador",
    "rolf": "Respuesta a algo gracioso",
    "sheesh": "ligera desaprobación"
}

print("Escribe en minúscula las palabras ")

for i in range (5): #bucle
    word = input("Escribe una palabra que no entiendas")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("No tenemos la palabra")
