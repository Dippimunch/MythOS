import pickle, generators


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
