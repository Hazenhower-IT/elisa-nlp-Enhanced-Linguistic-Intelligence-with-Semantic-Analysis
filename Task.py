import datetime
from Speak import Say


# Functions
# 2 Types

# 1 - Non Input

def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)

def Date():
    date = datetime.date.today()
    
    formatted_date = date.strftime("%d %B %Y")

    month_names = {
        "January": "gennaio", 
        "February": "febbraio", 
        "March": "marzo", 
        "April": "aprile", 
        "May": "maggio", 
        "June": "giugno", 
        "July": "luglio", 
        "August": "agosto", 
        "September": "settembre", 
        "October": "ottobre", 
        "November": "novembre", 
        "December": "dicembre"
    }

    month = date.strftime("%B")

    italian_month = month_names[month]

    formatted_date = formatted_date.replace(month, italian_month)

    Say(formatted_date)

def OpenFacebook():
    import webbrowser
    url = "https://www.facebook.com"
    Say("Certo! Apro subito facebook")
    webbrowser.open(url)

def OpenLinkedin():
    import webbrowser
    url = "https://www.linkedin.com"
    Say("Certo! Apro subito linkedin")
    webbrowser.open(url)

def OpenGithub():
    import webbrowser
    url = "https://www.github.com"
    Say("Certo! Apro subito github")
    webbrowser.open(url)

def Screenshot():
    import pyautogui
    screen = pyautogui.screenshot()
    name = "screen.png"
    screen.save("C:\Downloads\\" + name)
    Say("Screen Salvato Nella Cartella Downloads")




def NonInputExecution(query):
    query = str(query)

    if "time" in query:
        Time()
    elif "date" in query:
        Date()
    
    elif "facebook" in query:
        OpenFacebook()
    elif "linkedin" in query:
        OpenLinkedin()
    elif "github" in query:
        OpenGithub()
    
    elif "screenshot" in query:
        Screenshot()

# 2 - Input

def InputExecution(tag, query):

    if "wikipedia" in tag:
        name = str(query).replace("chi è","").replace("cos'è","").replace("cosa sono","").replace("chi era","").replace("chi erano","").replace("cerca info su","").replace("parlami di","").replace("wikipedia","")
        import wikipedia
        wikipedia.set_lang("it")
        result = wikipedia.summary(name)
        Say(result)

    elif "google" in tag:
        query = str(query)
        query = query.replace("cerca","")
        query = query.replace("cerca su google","")
        query = query.replace("google","")
        import pywhatkit
        Say("Avvio subito una ricerca su google")
        pywhatkit.search(query)

    elif "youtube" in tag:
        song = str(query)
        song = song.replace("metti","")
        song = song.replace("youtube","")
        song = song.replace("voglio sentire","")
        import pywhatkit
        Say("Riproduco " + song + ". Maestro, musica")
        pywhatkit.playonyt(song)
