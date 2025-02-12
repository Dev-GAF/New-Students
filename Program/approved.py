import pyautogui
import pandas as pd
import time
import pyperclip

from datetime import date

pyautogui.PAUSE = 2

def login_gmail () -> None:
    # Step 1: Open Gmail.
        # https://gmail.com/
    # NOTE: Since I have multiple accounts, I will adapt them for this.

    # Opening the Browser:
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")

    # Entering the URL
    pyautogui.write("https://gmail.com/")
    pyautogui.press("enter")

    # Step 2: Log in.
    time.sleep(5)

    pyautogui.click(x=834, y=513)
    pyautogui.press("enter")

    time.sleep(1)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("delete")

    # Password
    pyautogui.write("password")
    pyautogui.press("enter")

def import_data () -> pd.DataFrame:
    # Step 3: Import the data of the applicants.
    
    table = pd.read_csv("Database/Vestibulandos.csv", encoding="ISO-8859-1")
    # Encoding 'ISO-8859-1' (also known as latin1), handles a wider range of special characters.

    print(table)
    
    return table

def prepare_email (table: pd.DataFrame, row: int) -> str:
    # Step 4: Prepare the Email that will be sent.
    
    applicant = table.loc[row, "nome_completo"]
    institution = "Automatizando Coisas"
    year = date.today().strftime('%Y')
    
    pyautogui.write(f"[{institution}] applicant {year}")
    pyautogui.press("tab")
    
    time.sleep(5)
    
    body = f'''
    Prezado {applicant}.
    
    É com grande satisfação que a {institution} vem parabenizá-lo(a) pela sua aprovação no vestibulinho! Este é um momento de grande importância e uma verdadeira conquista que reflete todo o seu esforço, dedicação e comprometimento.
    
    O ingresso no vestibulinho representa uma nova etapa em sua trajetória educacional, cheia de oportunidades e desafios. Estamos confiantes de que você continuará a se destacar, buscando sempre o aprimoramento e o aprendizado, e que essa conquista será o início de muitas outras.
    
    A {institution} se orgulha de tê-lo(a) como parte de nossa comunidade e estará à disposição para apoiá-lo(a) em cada passo dessa nova jornada. Desejamos muito sucesso e que você aproveite ao máximo todas as oportunidades que surgirão ao longo do seu caminho.
    
    Parabéns mais uma vez e conte conosco para o que precisar!
    
    Atenciosamente,
    
    Roberto Luiz
    Diretor Geral
    
    [{institution}]
    '''
    
    return body

def send_email (table: pd.DataFrame) -> None:
    # Step 5: Send the Email to the Approved Applicants.
    time.sleep(10)
    
    for row in table.index:
        status = table.loc[row, "situacao"].upper()
        if status == "APROVADO":
            pyautogui.click(x=85, y=218)
            
            pyautogui.write(table.loc[row, "email"])
            
            pyautogui.click(x=922, y=358)
            pyautogui.press("tab")
            
            email_body = prepare_email(table, row)
            pyperclip.copy(email_body)
            pyautogui.hotkey("ctrl", "v")
            
            pyautogui.click(x=783, y=687)
            
            time.sleep(5)
