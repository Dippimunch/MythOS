import pickle, generators
import tkinter as tk
from tkinter import filedialog


# NEW
    # INITIALIZE
    # NAME
        # default/ find if files same name, add +=1 to filename if so/ repeat

def new_lang_rand():
    language = generators.randomLanguage()
    print(language.words)
    return language
    
    

# LOAD
# world = state.world



# SAVE
# just a single language, for now
def save(language):
    f = open ("language_save_file.txt", "wb")
    print(f)
    pickle.dump(language, f)
    f.close()




def load():
    root = tk.Tk()
    file = filedialog.askopenfile(parent=root,mode='rb',title='Choose a file')
    if file:
        data = file.read()
        file.close()
        print("I got %d bytes from this file." % len(data))

    """f = open ("language_save_file.txt", "rb")
    print(pickle.load(f))
    f.close()"""
