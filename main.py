import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit

audio = sr.Recognizer()
maquina = pyttsx3.init()


def execulta_comando():
    try:
        with sr.Microphone() as source:
            print(f'Ouvindo...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'leticia' in comando:
                comando = comando.replace('leticia', '')
                maquina.say(comando)
                maquina.runAndWait()

    except ValueError:
        print(f'Microfone não está ok')
    return comando


def comando_voz_usuario():
    comando = execulta_comando()
    if 'horas' in comando:  # biblioteca datetime
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('agora são' + hora)
        maquina.runAndWait()

    elif 'procure por' in comando:  # API da Wikipédia para Python
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, 2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()

    elif 'toque' in comando:  # biblioteca pywhatkit
        musica = comando.replace('toque', '')
        pywhatkit.playonyt(musica)
        maquina.say('tocando musica')
        maquina.runAndWait()


comando_voz_usuario()
