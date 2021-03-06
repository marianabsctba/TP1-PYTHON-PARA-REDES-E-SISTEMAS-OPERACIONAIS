#QUESTÃO 12 - Indique uma maneira de criar um processo externo ao seu programa usando o módulo ‘os’ e usando o módulo ‘subprocess’ de Python.
#Dê um exemplo de cada.

import os, subprocess

user_file = os.path.basename(__file__) # pega o nome do arquivo atual (só uma solução alternativa para o exercício)

# exemplo 1

# poderia ser usado o os.spawn também.

def create_process_os(user_file):
    return os.system(f"notepad {user_file}")

# exemplo 2

def create_subprocess(user_file):
    return subprocess.run(["notepad", f"{user_file}"])

def create_spawn(): # criado notepad em branco externamente
    execut = os.environ['SYSTEMROOT'] + '\\System32\\notepad'
    os.spawnl(os.P_NOWAIT, execut, " ")


create_process_os(user_file)
create_subprocess(user_file)
create_spawn(user_file)
