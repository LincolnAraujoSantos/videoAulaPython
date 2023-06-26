import platform
from datetime import datetime
import getpass

#platform
print("Distribuição do Sistema Operacional.: ", platform.platform())
print("Nome do Sistema Operacional.........: ", platform.system())
print("Versão do Sistema Operacional.......: ", platform.release())
print("Arquitetura.........................: ", platform.architecture())
print("Nome do Computador..................: ", platform.node())
print("Tipo de Máquina.....................: ", platform.machine())
print("Processador.........................: ", platform.processor())
print("Versão do Python....................: ", platform.python_version())

#PLATFORM() metdo que retorna a distribuição exata do sistema
#SYSTEM() retorna o a qual sistema operacional que esta sendo executado
#REALEASE() retorna a versao do sistema operacional que esta sendo executado
#ARCHITETURE() arquitetura que esta em uso pela maquina
#NODE() retorna o nome do computador na rede
#MACHINE() retorna o tipo de maquina, muito utilizado com o metodo PROCESSOR(), que retorna o processador que esta sendo executado
#PYTHON_VERSION() retorna a versao do python que esta sendo executada

#datetime
print(datetime.now())

