import os
import shutil
Pedir_caminho = input("Copie e cole o endereço da pasta: ")
downloads = os.path.join(Pedir_caminho)
destino = os.path.join(downloads, "PDFs")
destino2 = os.path.join(downloads, "webp")
destino3 = os.path.join(downloads, "PNGs")
destino4 = os.path.join(downloads, "Mp3s")



os.makedirs(destino, exist_ok=True)
os.makedirs(destino2, exist_ok=True)
os.makedirs(destino3, exist_ok=True)
os.makedirs(destino4, exist_ok=True)





if os.path.exists(downloads):
    for dirpath, dirnames, filenames in os.walk(downloads):
        for file in filenames:
            if file.endswith('.pdf'):
                origem = os.path.join(dirpath, file)
                shutil.move(origem, destino)
                
            elif file.endswith('.webp'):
                origem2 = os.path.join(dirpath, file)
                shutil.move(origem2, destino2)
            elif file.endswith('.png'):
                origem3 = os.path.join(dirpath, file)
                shutil.move(origem3, destino3 )
            elif file.endswith('.mp3'):
                origem4 = os.path.join(dirpath, file)
                shutil.move(origem4, destino4 )


else:
    print("A pasta Downloads não foi encontrada!")
