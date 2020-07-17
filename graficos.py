from datetime import datetime
import matplotlib.pyplot as plt
import json
import os


files = os.listdir('./logs-reais') # pega todos os nomes dos arquivos desse diretorio
files_sorted = [] # lista ja com os timestamps em int e ordenados (ascendente)

hour = [] # lista com as horas de captura dos logs
total_per_hour = [] # lista com totais de registro por hora 

# listas para totais individuais de cada boi
total_caprichoso = [0] * 476
total_garantido = [0] * 476

# contadores
cont_caprichoso = 0
cont_garantido = 0

# converte para inteiro o timestamp registrado como  nome do arquivo
for i in range(0, len(files)):
    timestamp = int(files[i].split('.')[0])
    files_sorted.append(timestamp)

files_sorted.sort() # agora, de fato, ordena a lista 

# inicio do processamento dos arquivos de log
print('-> Os arquivos de log comecarao a ser lidos')
for i in range(0, len(files_sorted)):

    rel = open('logs-reais/' + str(files_sorted[i]) + '.json', 'r')
    hour_collected = datetime.fromtimestamp(files_sorted[i]/1000.0)
    rel_content = json.loads(rel.read())

    # separando totais de registro por boi
    for j in range(0, len(rel_content)):
        time = rel_content[j].get('time')
        if time == 0:
            cont_caprichoso += 1
            total_caprichoso[i] = cont_caprichoso 
        elif time == 1:
            cont_garantido += 1
            total_garantido[i] = cont_garantido

    cont_caprichoso = 0
    cont_garantido = 0

    print(hour_collected, len(rel_content))
    hour.append(hour_collected)
    total_per_hour.append(len(rel_content))
    rel.close()
print('-> Terminou de ler os arquivos de log')


plt.plot(hour, total_per_hour)
plt.show()

plt.plot(hour, total_caprichoso)
plt.show()

plt.plot(hour, total_garantido)
plt.show()

