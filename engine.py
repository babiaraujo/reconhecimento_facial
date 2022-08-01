import face_recognition as fr

def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto)
    if(len(rostos) > 0 ):
        return True, rostos

    return False, []

def get_rostos():
    rostos_conhecidos = []
    nomes_dos_rostos = []

    babi2 = reconhece_face("./img/babi2.png")
    if(babi2[0]):
        rostos_conhecidos.append(babi2[1][0])
        nomes_dos_rostos.append("Babi")

    andre = reconhece_face("./img/andre.png")
    if(andre[0]):
        rostos_conhecidos.append(andre[1][0])
        nomes_dos_rostos.append("André")

    return rostos_conhecidos, nomes_dos_rostos