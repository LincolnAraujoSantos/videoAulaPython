arquivo = open("primeiro_arquivo.txt","w")

arquivo.write("Meu primeiro arquivo!")

arquivo.close()

arquivo = open("primeiro_arquivo.txt","a")

arquivo.write("\nMeu primeiro arquivo! Agora usando a função <a> append ")

arquivo.close()
