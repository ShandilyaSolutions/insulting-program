from gtts import gTTS
from playsound import playsound
import os

# text_val = 'At your service boss.'


def bolo(text_val):
    # Here are converting in English Language
    language = 'en'

    # Passing the text and language to the engine,
    # here we have assign slow=False. Which denotes
    # the module that the transformed audio should
    # have a high speed
    obj = gTTS(text=text_val, lang=language, slow=False)

# Here we are saving the transformed audio in a mp3 file named
# exam.mp3
    obj.save("exam.mp3")

# Play the exam.mp3 file
    playsound("exam.mp3")

# Remove the mp3 file after speaking (This stops the wastage of memory)
    os.remove("exam.mp3")




if __name__ == '__main__':
    bolo('Yay, I can speak')