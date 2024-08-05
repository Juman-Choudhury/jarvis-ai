import speech_recognition as sr
import pyttsx3

def speak(text: str):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__": 
    engine = pyttsx3.init()
    recognizer = sr.Recognizer()

    # Use the microphone as the source of input
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)
            print("Audio captured.")
        except sr.WaitTimeoutError:
            print("Listening timed out.")
            exit()

    # Recognize speech using Google Web Speech API
    try:
        print("Recognizing...")
        word = recognizer.recognize_google(audio)
        print(word)
        
        if word.lower() in ["hey jarvis", "jarvis"]:
            print("Hello, how may I help you?")
            speak("Hello, how may I help you...")
            
            while True:  # Continuous listening loop
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source)
                    print("Listening...")
                    try:
                        commandtoInit = recognizer.listen(source, timeout=2, phrase_time_limit=1)  # Added phrase_time_limit
                        print("Audio captured.")
                        command_textToinit = recognizer.recognize_google(commandtoInit)
                        if command_textToinit .lower() == "jarvis":
                            print("yah...")
                            speak("yah...")


                            print("Listening...")
                            command = recognizer.listen(source, timeout=3, phrase_time_limit=5)  # Added phrase_time_limit
                            print("Audio captured.")
                            command_text = recognizer.recognize_google(command)
                            if command_text.lower() == "exit":
                                print("Exiting the program.")
                                speak("Exiting the program.")
                                exit()  # Exit the program
                            else:
                                print(f"Command received: {command_text}")
                                speak(command_text)
                    
                    except sr.WaitTimeoutError:
                        print("Listening timed out.")
                        continue  # Continue listening instead of exiting

    except sr.UnknownValueError:
        print("Google Web Speech API could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")
