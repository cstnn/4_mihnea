# Import libraries
from nltk.chat.util import Chat, reflections

# Define conversation pairs
pairs = [
    # Static predefined answers
    ['my name is Costin', ['hi Costin, how are you ?\n']],
    ['quit', ['see you soon !\n']],
    
    # Dynamic answers
    ['my name is (.*)', ['hi %1, how are you ?\n']],
    ['great(.*)', ['glad to hear that !\n']],
    ['what is your name(.*)|what\'s your name(.*)', ['my name is \"Chat A. Lot\"\n']],
    ['(.*)created you(.*)', ['I was created by Costin N.\n']],
    ['(.*)help(.*)', ['Please tell me how can I help you\n']],
    
    # Static predefined random answers
    ['(hi|hello|hey)', ['hey there\n', 'hi there\n', 'yellow\n']],
]

# Initiate chatbot
try:
    print("--------------------------------------------------------------")
    print("I am a humble chatbot that was created to help you !")
    chat = Chat(pairs,reflections)
    chat.converse()
except Exception as e:
    print("--------------------------------------------------------------")
    print("[!] Conversation has been closed due to an ERROR:\n" + e)