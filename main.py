
import openai
import subprocess
from colorama import Fore, Style
import pwinput
import os
from dotenv import load_dotenv


def askquestion(question, engine):
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=question,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text
    print('\n' + Fore.BLUE+'Respuesta: ' +
          Style.RESET_ALL + Fore.GREEN+response + '\n')


load_dotenv()
if __name__ == "__main__":
    key = os.getenv("TOKEN")
    print(Fore.GREEN + 'Grupo firma \n' + Style.RESET_ALL)

    if not key:
        print(
            '\nSe necesita una API key, la puedes obtener desde aca '
            + Fore.BLUE + 'https://beta.openai.com/account/api-keys' + Style.RESET_ALL)
        key = pwinput.pwinput(prompt='\nLa API key: ', mask='*')
    openai.api_key = key
    model_engine = 'text-davinci-003'
    while True:
        print(
            Fore.BLUE +
            'Opciones: \n\t1: Abrir visual (para preguntas de mas de una linea) \n\t2: Pregnta alguna wea'
            + Style.RESET_ALL)

        option = int(input('Elige opcion: '))

        question = None
        if option == 1:
            print(Fore.RED + 'Aun estoy en eso' + Style.RESET_ALL)
            try:
                print(Fore.GREEN + 'abriendo Visual Studio Sode' + Style.RESET_ALL)
                subprocess.run(["code", "-w", "lineas.txt"], check=True)
            except:
                print(
                    Fore.RED + 'PROBLEMA ABRIENDO VISUAL CODE ... ABRIENDO NOTEPAD.EXE'+Style.RESET_ALL)
                subprocess.run(["notepad.exe", "lineas.txt"], check=True)
            with open("./lineas.txt", "r") as c:
                contents = c.read()
            print(Fore.BLUE + 'Pregunta: ' + Style.RESET_ALL +
                  Fore.GREEN + str(contents))
            question = contents
        elif option == 2:
            question = input('Pregunta algo: ')
        else:
            print(Fore.RED + 'Aun estoy en eso' + Style.RESET_ALL)

        if question:
            askquestion(question, model_engine)
