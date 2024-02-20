import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yp
import pyjokes
import webbrowser
import datetime
import wikipedia


def transformar_audio_en_texto():
    # alamacenar recognizer en variable
    r = sr.Recognizer()

    # configurar microfono
    with sr.Microphone() as origen:
        # tiempo espera al microfono
        r.pause_threshold = 0.8
        # informar que come zo la grabacion
        print('ya puedes hablar')
        # guardar en la variable lo que escuche como audio
        audio = r.listen(origen)

        try:
            pedido = r.recognize_google(audio)

            # pruebad de que pudo ingresar
            print('Dijiste: ' + pedido)

            # devolver pedido
            return pedido

        # en caso que no comprenda el audio
        except sr.UnknownValueError:
            # prueba de que no comprendo audio
            print('ups, no entendi')

            # devolver error
            return 'sigo esperando'

        # en caso de no resolver el pedido

        except sr.RequestError:
            # prueba de que no comprendo el audio
            print('ayy, no logro comprenderlo')

            return 'sigo esperando'

        # error inesperado
        except:
            print('ups algo salio mal')

            return 'algo sucedio'


transformar_audio_en_texto()
