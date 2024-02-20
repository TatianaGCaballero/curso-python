import cv2
import face_recognition as fr

# cargar imagenes
foto_control = fr.load_image_file('FotoA.jpg')
foto_prueba = fr.load_image_file('FotoB.jpg')

# pasar imagen a rgb
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# localizar cara a
lugar_cara_a = fr.face_locations(foto_control)[0]
# codificar cara
cara_codificada_a = fr.face_encodings(foto_control)[0]

# ubicacion cara
print(lugar_cara_a)

# mostrar rectangulo

cv2.rectangle(foto_control,
              (lugar_cara_a[3], lugar_cara_a[0]),
              (lugar_cara_a[1], lugar_cara_a[2]),
              (0,255,0),
              2)

# localizar cara b
lugar_cara_b = fr.face_locations(foto_prueba)[0]
# codificar cara
cara_codificada_b = fr.face_encodings(foto_prueba)[0]

# ubicacion cara
print(lugar_cara_b)

# mostrar rectangulo

cv2.rectangle(foto_prueba,
              (lugar_cara_b[3], lugar_cara_b[0]),
              (lugar_cara_b[1], lugar_cara_b[2]),
              (0,255,0),
              2)

# realizar comparacion
resultado = fr.compare_faces([cara_codificada_a], cara_codificada_b)
print(resultado)


# medida distancia
distancia = fr.face_distance([cara_codificada_a], cara_codificada_b)
print(distancia)

# mostrar distancia en la foto
cv2.putText(foto_prueba,
            f'{resultado} {distancia.round(2)}',
            (50,50),
            cv2.FONT_ITALIC,
            1,
            (0,255,0),
            2
            )

# mostrar imagenes
cv2.imshow('Foto control', foto_control)
cv2.imshow('Foto prueba', foto_prueba)

# mantener programa abierto
cv2.waitKey(0)
