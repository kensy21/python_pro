meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print("Esta palabra si la tenemos en nuestra lista, vas hacer una muy buena persona")
    print(meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print(" Esta no la tenemos😭😭 ya tu mami no te quiere")
