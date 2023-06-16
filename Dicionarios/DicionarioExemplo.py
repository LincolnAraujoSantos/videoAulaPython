usuarios = {}
print(usuarios)

usuarios = {"José" :["José da Silva", "24/12/2017", "Mecanica"],
            "João": ["João das Neves", "20/12/2017", "Oficina"]}
print(usuarios)

usuarios["Pedro"] =  ["Pedro dos Santos", "24/12/2017", "Recepção"]
print(usuarios)

print("####----####")
print(usuarios.get("João"))