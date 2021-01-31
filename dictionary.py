import random
import csv


locations = ['settlement', 'nature']
size_mod = ['very small', 'small', 'medium', 'large', 'very large']

def add(word, target):
    target.append(word)
    print('Added \'%s\'   %s' % (word, 'list'))

# I forget how exactly this works
def filterTheDict(dictObj, callback):
    newDict = dict()
    # Iterate over all the items in dictionary
    for (key, value) in dictObj.items():
        # Check if item satisfies the given condition then add to new dict
        if callback((key, value)):
            newDict[key] = value
    return newDict

def pick(category):
    return random.choice(list(filterTheDict(swadesh, lambda elem: elem[1] == category)))

# based on pg33 AoLI
# need voiced
def consonant_chart():
    chart = []
    row = ['oral stop', 'fricative', 'affricate', 'nasal stop', 'glide', 'flap/tap', 'trill', 'lateral']
    column = ['labial', 'dental', 'alveolar', 'retroflex', 'palatal', 'velar', 'uvular', 'glottal']
    blanks = [[7, 2], [7, 3], [1, 4], [6, 4], [7, 4], [0, 5], [1, 5], [4, 5], [5, 5], [6, 5], [7, 5],
              [1, 6], [3, 6], [4, 6], [5, 6], [7, 6], [0, 7], [6, 7], [7, 7]]

    for c in range(8):
        for r in range(8):
            if [c, r] not in blanks:
                chart.append("%s %s" % (column[c], row[r]))
    
    return chart
                         
swadesh = {'one': 'number', 'two': 'number', 'three': 'number', 'four': 'number', 'five': 'number',
           'I': 'pronoun', 'you': 'pronoun', 'he': 'pronoun', 'we': 'pronoun', '''y'all''': 'pronoun', 'they': 'pronoun', 'this': 'pronoun', 'that': 'pronoun',
           'here': 'pronoun', 'there': 'pronoun', 'who': 'pronoun', 'what': 'pronoun', 'where': 'pronoun', 'when': 'pronoun', 'how': 'pronoun',
           'not': 'adverb', 'woman': 'noun', 'man': 'noun',
           'human': 'noun', 'child': 'noun', 'wife': 'noun', 'husband': 'noun', 'mother': 'noun', 'father': 'noun', 'animal': 'noun', 'fish': 'noun', 'bird': 'noun',
           'dog': 'noun', 'louse': 'noun', 'snake': 'noun', 'worm': 'noun', 'tree': 'noun', 'forest': 'noun', 'stick': 'noun', 'fruit': 'noun', 'seed': 'noun',
           'leaf': 'noun', 'root': 'noun', 'bark': 'noun', 'flower': 'noun', 'grass': 'noun', 'rope': 'noun', 'skin': 'noun', 'meat': 'noun', 'blood': 'noun',
           'bone': 'noun', 'fat': 'noun', 'egg': 'noun', 'horn': 'noun', 'tail': 'noun', 'feather': 'noun', 'hair': 'noun', 'head': 'noun', 'ear': 'noun',
           'eye': 'noun', 'nose': 'noun', 'mouth': 'noun', 'tooth': 'noun', 'tongue': 'noun', 'fingernail': 'noun', 'foot': 'noun', 'leg': 'noun', 'knee': 'noun',
           'hand': 'noun', 'wing': 'noun', 'belly': 'noun', 'guts': 'noun', 'neck': 'noun', 'back': 'noun', 'breast': 'noun', 'heart': 'noun', 'liver': 'noun',
           'sun': 'noun', 'moon': 'noun', 'star': 'noun', 'water': 'noun', 'rain': 'noun', 'river': 'noun', 'lake': 'noun', 'sea': 'noun', 'salt': 'noun',
           'stone': 'noun', 'sand': 'noun', 'dust': 'noun', 'earth': 'noun', 'cloud': 'noun', 'fog': 'noun', 'sky': 'noun', 'wind': 'noun', 'snow': 'noun',
           'ice': 'noun', 'smoke': 'noun', 'fire': 'noun', 'ash': 'noun', 'road': 'noun', 'mountain': 'noun', 'name': 'noun', 'night': 'noun', 'day': 'noun',
           'year': 'noun',
           'red': 'adjective', 'all': 'adjective', 'many': 'adjective', 'some': 'adjective', 'few': 'adjective', 'other': 'adjective', 'big': 'adjective',
           'long': 'adjective', 'wide': 'adjective', 'thick': 'adjective', 'heavy': 'adjective', 'small': 'adjective', 'short': 'adjective', 'narrow': 'adjective',
           'thin': 'adjective', 'green': 'adjective', 'yellow': 'adjective', 'white': 'adjective', 'black': 'adjective', 'warm': 'adjective', 'cold': 'adjective',
           'full': 'adjective', 'new': 'adjective', 'old': 'adjective', 'good': 'adjective',
           'bad': 'adjective', 'rotten': 'adjective', 'dirty': 'adjective', 'straight': 'adjective', 'round': 'adjective', 'sharp': 'adjective', 'dull': 'adjective',
           'smooth': 'adjective', 'wet': 'adjective', 'dry': 'adjective', 'correct': 'adjective', 'near': 'adjective', 'far': 'adjective', 'right': 'adjective',
           'left': 'adjective',
           'at': 'preposition', 'in': 'preposition', 'with': 'preposition', 'and': 'preposition', 'if': 'preposition', 'because': 'preposition',
           'burn': 'verb', 'drink': 'verb', 'eat': 'verb', 'bite': 'verb', 'suck': 'verb', 'spit': 'verb', 'vomit': 'verb', 'blow': 'verb', 'breathe': 'verb',
           'laugh': 'verb', 'see': 'verb', 'hear': 'verb', 'know': 'verb', 'think': 'verb', 'smell': 'verb', 'fear': 'verb', 'sleep': 'verb', 'live': 'verb',
           'die': 'verb', 'kill': 'verb', 'fight': 'verb', 'hunt': 'verb', 'hit': 'verb', 'cut': 'verb', 'split': 'verb', 'stab': 'verb', 'scratch': 'verb',
           'dig': 'verb', 'swim': 'verb', 'fly': 'verb', 'walk': 'verb', 'come': 'verb', 'lie': 'verb', 'sit': 'verb', 'stand': 'verb', 'turn': 'verb',
           'fall': 'verb', 'give': 'verb', 'hold': 'verb', 'squeeze': 'verb', 'rub': 'verb', 'wash': 'verb', 'wipe': 'verb', 'pull': 'verb', 'push': 'verb',
           'throw': 'verb', 'tie': 'verb', 'sew': 'verb', 'count': 'verb', 'say': 'verb', 'sing': 'verb', 'play': 'verb', 'float': 'verb', 'flow': 'verb',
           'freeze': 'verb', 'swell': 'verb'}

alt = {
    'Amount',
    'Argument',
    'Art',
    'Be',
    'Beautiful',
    'Belief',
    'Cause',
    'Certain',
    'Chance'
    'Change',
    'Clear',
    'Common',
    'Comparison',
    'Condition',
    'Connection',
    'Copy',
    'Decision',
    'Degree',
    'Desire',
    'Development',
    'Different',
    'Do',
    'Education',
    'End',
    'Event',
    'Examples',
    'Existence',
    'Experience',
    'Fact',
    'Fear',
    'Feeling',
    'Fiction',
    'Force',
    'Form',
    'Free',
    'General',
    'Get',
    'Give',
    'Good',
    'Government',
    'Happy',
    'Have',
    'History',
    'Idea',
    'Important',
    'Interest',
    'Knowledge',
    'Law',
    'Let',
    'Level',
    'Living',
    'Love',
    'Make',
    'Material',
    'Measure',
    'Mind',
    'Motion',
    'Name',
    'Nation',
    'Natural',
    'Necessary',
    'Normal',
    'Number',
    'Observation',
    'Opposite',
    'Order',
    'Organization',
    'Part',
    'Place',
    'Pleasure',
    'Possible',
    'Power',
    'Probable'
    'Property',
    'Purpose',
    'Quality',
    'Question',
    'Reason',
    'Relation',
    'Representative',
    'Respect',
    'Responsible',
    'Right',
    'Same',
    'Say',
    'Science',
    'See',
    'Seem',
    'Sense',
    'Sign',
    'Simple',
    'Society',
    'Sort',
    'Special',
    'Substance',
    'Thing',
    'Thought',
    'True',
    'Use',
    'Way',
    'Wise',
    'Word',
    'Work'
}

def test():
    print(pick('adjective'), pick('noun'), pick('verb'), pick('noun'))

