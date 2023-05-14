import speech_recognition as sr #pip install speechrecognition

def Listen():
    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("In Ascolto...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 10)
    
    try:
        print("Caricando...")
        query = r.recognize_google(audio, language="IT-IT")
        print(f"Hai Detto : {query}")
    
    except:
        return ""
    

    query = str(query)
    return query.lower()


