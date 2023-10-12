from PIL import Image
import os
import time

print()



def convert(format, image_name):
    data = Image.open(f"./images d'entrée/{image_name}", "r")
    data.save(f"./images de sortie/{image_name.split('.')[0]}.{format.lower()}", format.upper())
    print(image_name, "convertie avec succès")
    return 1

def ask_image_format():
    formats = ["PNG", "JPEG", "JPG", "BMP", "GIF", "TIFF", "ICO", "WEBP", "PPM", "PGM", "PBM", "EPS", "PCX", "IM", "RGB"]
    print()
    print("ATTENTION certains formats ne peuvent pas être convertis en certains autres formats")
    print()
    format = input("Vers quel format d'image voulez-vous convertir (entrez 'infos' pour voir les formats disponnible)? ")
    if format == "infos":
        print("""\n
            PNG: Portable Network Graphics \n 
            JPEG: Joint Photographic Experts Group \n 
            JPG: Une extension alternative pour les fichiers JPEG \n 
            BMP: Bitmap \n 
            GIF: Graphics Interchange Format \n 
            TIFF: Tagged Image File Format \n 
            ICO: Icon format \n 
            WEBP: Format d'image WebP \n 
            PPM: Portable Pixmap Format \n 
            PGM: Portable Graymap Format \n 
            PBM: Portable Bitmap Format \n 
            EPS: Encapsulated PostScript \n 
            PCX: Picture Exchange \n 
            IM: a format \n 
            RGB: Raw red, green, and blue samples \n """)
        ask_image_format()
    if format.upper() in formats:
        return format
    else:
        print()
        print("ATTENTION !")
        print()
        print("Ce format n'est pas reconnu ou n'est pas pris en charge !")
        print()
        ask_image_format()

def start_app():

    total_images_traitee = 0
    image_success = 0
    image_failled = 0

    dir_path = "./images d'entrée"

    if len(os.listdir(dir_path)) < 1:
        print()
        print(f"le dossier '{dir_path}' est vide")
    else:

        format = ask_image_format()

        for image_name in os.listdir(dir_path):

            total_images_traitee += 1

            if image_name.split(".")[1] == format:
                print()
                print(f"L'image '{image_name}' est déjà au format {format}")
                print()
                image_failled += 1
                continue

            if image_name.split(".")[-1] == "svg" or image_name.split(".")[-1] == "SVG":
                print()
                print(f"ATTENTION ! Les 'svg' ne peuvent pas être convertis !")
                print()
                image_failled += 1
                continue

            
            try:
                image_success += convert(format, image_name)
            except:
                print()
                print(f"Un problème est survenue avec '{image_name}'")
                image_failled += 1
            print()

    print()
    print(f"Images traitées: {total_images_traitee}")
    print(f"Images converties: {image_success}")
    print(f"Images non-converties: {image_failled}")

while True:
    start_app()