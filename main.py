meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            'LMAO':'Respuesta que se usa para expresar risa'
            }
print('Hola, bienvenido a mi diccionario')
for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print('No existe esa palabra en el diccionario')
