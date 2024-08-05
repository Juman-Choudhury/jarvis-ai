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
        recognizer.adjust_for_ambient_noise(source,duration=2)
        print("Listening for trigger phrase...")

        try:
            # Continuous listening for trigger phrase
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)
                print("Audio captured.")
                try:
                    print("Recognizing...")
                    word = recognizer.recognize_google(audio)
                    print(word)

                    if word.lower() in ["hey jarvis", "jarvis"]:
                        print("Hello, how may I help you?")
                        speak("Hello, how may I help you...")

                        # Continuous command listening loop
                    while True:
                        print("Adjusting for ambient noise, please wait...")
                        recognizer.adjust_for_ambient_noise(source,duration=2)
                        print("Listening for commands...")
                        try:
                                commandtoInit = recognizer.listen(source, timeout=20, phrase_time_limit=1)
                                print("Audio captured.")
                                command_textToinit = recognizer.recognize_google(commandtoInit).lower()

                                if command_textToinit == "jarvis":
                                    print("yah...")
                                    speak("yah...")

                                    print("Listening for further commands...")
                                    command = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                                    print("Audio captured.")
                                    command_text = recognizer.recognize_google(command)

                                    if command_text.lower() == "exit":
                                        print("Exiting the program.")
                                        speak("Exiting the program.")
                                        exit(0)  # Exit the program
                                    else:
                                        print(f"Command received: {command_text}")
                                        speak(command_text)

                        except sr.WaitTimeoutError:
                                print("Listening timed out.")
                                continue  # Continue listening instead of exiting
                        except sr.UnknownValueError:
                                print("Google Web Speech API could not understand the audio")
                                continue  # Continue listening instead of exiting
                        except sr.RequestError as e:
                                print(f"Could not request results from Google Web Speech API; {e}")
                                continue  # Continue listening instead of exiting

                except sr.UnknownValueError:
                    print("Google Web Speech API could not understand the audio")
                except sr.RequestError as e:
                    print(f"Could not request results from Google Web Speech API; {e}")

        except sr.WaitTimeoutError:
            print("Listening timed out.")
            exit()  # Exit if initial listening timed out
