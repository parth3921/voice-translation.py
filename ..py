import googletrans
import speech_recognition
import gtts
import playsound #librarys

input_lang = "hi"
output_lang = "en"


recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Speak Now")

    voice = recognizer.listen(source)
    text = recognizer.recognize_google(voice,language=input_lang) #here "hi" use for hindi 
    print(text)                                             #this line for input



  
# output 
    translator = googletrans.Translator()
    translation = translator.translate(text,dest=output_lang) #here "en" use for english
    print(translation.text)

    converted_audio = gtts.gTTS(translation.text, lang=output_lang)
    converted_audio.save("hello.mp3")
    playsound.playsound("hello.mp3")





'''import googletrans
print(googletrans.LANGUAGES)    THIS USED  FOR LANGAUAGE CODE  '''
