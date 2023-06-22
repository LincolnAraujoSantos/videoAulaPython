import json

dicionario = {
  "K8-1": ["KOMORI 8 CORES", "20/06/2023", "UNIDADE 1"],
  "K8-2": ["KOMORI 8 CORES", "21/06/2023", "UNIDADE 2"],
  "K5": ["KOMORI 5 CORES", "22/06/2023", "VERNIZ"]
}

with open("bd1.json","w") as json_file:#criação de arquivo antes de chama-lo
    json.dump(dicionario,json_file)