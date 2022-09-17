import os, time 

#Escolha o diretorio que o arquivo está 
a1 = r"C:\Users\Sorpe\Downloads"
now =time.time()

#Deleção do arquivo
    #Defina a função do comando, no meu caso "a1"
    
for filename in os.listdir(a1):
    #Defina quanto tempo o arquivo deverá permanecer na pasta até a exclusão, no meu caso até "15" dias
    if os.path.getatime(os.path.join(a1, filename)) < now - 5 * 86400:
        #Print dos arquivos com mais de 15 dias 
        if os.path.isfile(os.path.join(a1, filename)):
            print(filename)
            #Exclusão permanente de arquivos, cuidado! (Retire o "#" para habilitar)
            os.remove(os.path.join(a1, filename))



