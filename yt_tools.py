"""
Script download videos Youtube
Autor : Raul Braga
Bibliotecas usadas: PyTube, OS e Time
Date: 19/05/2023
"""

from pytube import YouTube
import os
import time

while True:
    print("|" + "=" * 5 + "[Y0uTub3 To0ls]" + "=" * 5 + "|")
    print("1 - Download video\n2 - Sair")
    option = input("Opção: ")
    if option.isnumeric():
        option = int(option)
        if option == 1:
            url = input(f"Link: ")
            os.system("cls")
            time.sleep(8)
            video = YouTube(url)
            print(f'Titulo: {video.title}')
            print(f'Duração: {video.length} segundos..')
            download_true = input("Realizar Download:  [s][n]")
            if download_true.isalpha():
                if download_true == "s":
                    video.streams.get_highest_resolution().download()
                else:
                    print("Ok, encerrando...")
            else:
                print("Erro..")
        else:
            print("Saindo..")
            break
    else:
        print("Error...")
