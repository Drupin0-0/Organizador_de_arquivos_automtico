import os
import shutil
Pedir_caminho = input("Copie e cole o endereço da pasta: ")
downloads = os.path.join(Pedir_caminho)
destinos = destino = os.path.join(downloads, "PDFs")
destino2 = os.path.join(downloads, "Webp")
destino3 = os.path.join(downloads, "PNGs")
destino4 = os.path.join(downloads, "Mp3s")
destino5 = os.path.join(downloads, "Imagens")
destino6 = os.path.join(downloads, "Documentos")
destino7 = os.path.join(downloads, "Planilhas")
destino8 = os.path.join(downloads, "Apresentações")
destino9 = os.path.join(downloads, "Compactados")
destino10 = os.path.join(downloads, "Vídeos")
destino11 = os.path.join(downloads, "Outros")

destinos = (
    destino, destino2, destino3, destino4, destino5, 
    destino6, destino7, destino8, destino9, destino10, destino11
)

for destino in destinos:
    os.makedirs(destino, exist_ok=True)



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
                shutil.move(origem3, destino3)

            elif file.endswith('.mp3'):
                origem4 = os.path.join(dirpath, file)
                shutil.move(origem4, destino4)

            elif file.endswith(('.jpg', '.jpeg', '.bmp', '.tiff')):
                origem5 = os.path.join(dirpath, file)
                shutil.move(origem5, destino5)

            elif file.endswith(('.doc', '.docx', '.odt', '.txt', '.rtf')):
                origem6 = os.path.join(dirpath, file)
                shutil.move(origem6, destino6)

            elif file.endswith(('.xls', '.xlsx', '.ods', '.csv')):
                origem7 = os.path.join(dirpath, file)
                shutil.move(origem7, destino7)

            elif file.endswith(('.ppt', '.pptx', '.odp')):
                origem8 = os.path.join(dirpath, file)
                shutil.move(origem8, destino8)

            elif file.endswith(('.zip', '.rar', '.7z', '.tar', '.gz')):
                origem9 = os.path.join(dirpath, file)
                shutil.move(origem9, destino9)

            elif file.endswith(('.mp4', '.avi', '.mkv', '.mov', '.wmv')):
                origem10 = os.path.join(dirpath, file)
                shutil.move(origem10, destino10)

            elif file.endswith(('.exe', '.msi', '.apk', '.iso')):
                origem11 = os.path.join(dirpath, file)
                shutil.move(origem11, destino11)



else:
    print("A pasta Downloads não foi encontrada!")
