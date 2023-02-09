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
    # print(Fore.GREEN + 'Busco pega \n' + Style.RESET_ALL)

    if not key:
        print(
            '\nSe necesita una API key, la puedes obtener desde aquí '
            + Fore.BLUE + 'https://beta.openai.com/account/api-keys' + Style.RESET_ALL)
        key = pwinput.pwinput(prompt='\nLa API key: ', mask='*')
    openai.api_key = key
    model_engine = 'text-davinci-003'
    while True:
        print(
            Fore.BLUE +
            'Opciones: \n\t1: Abrir visual (para preguntas de más de una línea) \n\t2: Pregunta alguna cosa'
            + Style.RESET_ALL)

        option = int(input('Elige opción: '))

        question = None
        if option == 1:
            print(Fore.RED + 'Aún estoy en eso' + Style.RESET_ALL)
            try:
                print(Fore.GREEN + 'Abriendo Visual Studio Code' + Style.RESET_ALL)
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
            print(Fore.RED + 'Aún estoy en eso' + Style.RESET_ALL)

        if question:
            askquestion(question, model_engine)
