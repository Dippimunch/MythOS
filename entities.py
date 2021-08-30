class Location:
    def __init__(self, name, size, climate, population):
        self.name = name
        self.size = size
        self.climate = climate
        self.population = population
        self.list = []

    def census(self):
        censusList = []
        for p in range(len(self.list)):
            censusList.append(self.list[p].name)
        print(censusList)
    
class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.inventory = []

    def move(self, target, speed):
        current = self.location
        # distance and speed
        self.location = target

class Language:
    def __init__(self, name, consonants, vowels, base, words, features={}):
        self.consonants = consonants
        self.vowels = vowels
        self.base = base
        self.words = words
        
        # Features *kwargs? How to reduce space
        # https://wals.info/feature

        # AREA
        # Phonology
        # ID/NAME/VALUE
        # {id: {feature: 'x', value: 'y'}}
        # featurization
        
class Culture:
    def __init__(self, name):
        self.name = name
        
        self.language = None
        """
        Language employed to manipulate others
        Language employed to misinform or mislead
        Language is translatable
        Abstraction in speech and thought
        Antonyms, synonyms
        Logical notions of "and", "not", "opposite", "equivalent", "part/whole", "general/particular"
        Binary cognitive distinctions
        Color terms: black, white
        Classification of: age, behavioral propensities, body parts, colors, fauna, flora, inner states, kin, sex, space, tools, weather conditions
        Continua (ordering as cognitive pattern)
        Discrepancies between speech, thought, and action
        Figurative speech, metaphors
        Symbolism, symbolic speech
        Synesthetic metaphors
        Tabooed utterances
        Special speech for special occasions
        Prestige from proficient use of language (e.g. poetry)
        Planning
        Units of time
        """

        self.social = None
        """
        Personal names
        Family or household
        Kin groups
        Peer groups not based on family
        Actions under self-control distinguished from those not under control
        Affection expressed and felt
        Age grades
        Age statuses
        Age terms
        Law: rights and obligations, rules of membership
        Moral sentiments
        Distinguishing right and wrong, good and bad
        Promise/oath
        Prestige inequalities
        Statuses and roles[3][4]
        Leaders
        De facto oligarchy
        Property
        Coalitions
        Collective identities
        Conflict
        Cooperative labor
        Gender roles
        Males on average travel greater distances over lifetime
        Marriage
        Husband older than wife on average
        Copulation normally conducted in privacy
        Incest prevention or avoidance, incest between mother and son unthinkable or tabooed
        Collective decision making
        Etiquette
        Inheritance rules
        Generosity admired, gift giving
        Mood- or consciousness-altering techniques and/or substances
        Redress of wrongs, sanctions
        Sexual jealousy
        Sexual violence
        Shame
        Territoriality
        Triangular awareness (assessing relationships among the self and two other people)
        Some forms of proscribed violence
        Visiting
        Trade
        """
        
        self.material = None
        """
        Shelter
        Control of fire
        Tools, tool making
        Weapons, spear
        Containers
        Cooking
        Lever
        Cordage
        """
        
        self.spiritual = None
        """    
        Magical thinking
        Use of magic to increase life and win love
        Beliefs about death
        Beliefs about disease
        Beliefs about fortune and misfortune
        Divination
        Attempts to control weather
        Dream interpretation
        Beliefs and narratives
        Proverbs, sayings
        Poetry/rhetorics
        Healing practices, medicine
        Childbirth customs
        Rites of passage
        Music, rhythm, dance, and to some degree associations between music and emotion
        Play
        Toys, playthings
        Death rituals, mourning
        Feasting
        Body adornment
        Hairstyles
        Art
        """

        # Human Universals (1991), Donald Brown
        
        
class Material(Culture):
    pass

class Spiritual(Culture):
    pass

class Social(Culture):
    pass
