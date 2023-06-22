import json

with open("bd.json", "r") as arq_json:
    dicionario = json.load(arq_json)
    for chave, dados in dicionario.items():
        print(chave + ":" + str(dados))

with open("bd.json", "a") as json_file:
    dicionario = {}
    dicionario.update({"K8-3": ["KOMORI 8 CORES", "20/06/2023", "UNIDADE 3"],
                       "K8-4": ["KOMORI 8 CORES", "21/06/2023", "UNIDADE 4"],
                       "K5-VERNIZ": ["KOMORI 5 CORES + VERNIZ", "22/06/2023", "VERNIZ"]})
    json.dump(dicionario, json_file)
