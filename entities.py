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
    def __init__(self, name, age, sex, lang, kin, location):
        self.name = name
        self.age = age
        self.sex = sex # gender
        #self.soc_class = soc_class
        self.lang = lang # languages = {'foo' : 1.0}
        self.kin = kin # {mother:'', father:'', ...}
        self.location = location
        self.inventory = []

    def move(self, target, speed):
        current = self.location
        # distance and speed
        self.location = target

class Plant:
    def __init__(self, name, germ_rate):
        self.name = name
        self.germ_rate = germ_rate
        # time to harvest
        # yield
        self.growth = 0
        self.part_color = {'flower':'white', 'leaf':'green', 'stem':'brown', 'fruit':'red'}
        self.part_edible = {'flower':True, 'leaf':False, 'stem':False, 'fruit':True}
        
        # root structure
        """Branch magnitude 	Number of links (exterior or interior)
        Topology 	Pattern of branching (Herringbone, Dichotomous, Radial)
        Link length 	Distance between branches
        Root angle 	Radial angle of a lateral root's base around the parent root's circumference, the angle of a lateral root from its parent root, and the angle an entire system spreads.
        Link radius 	Diameter of root """
        self.part_feat = {}
        # Habit
        #  Storage of carbs or water
        
        # Morphology
        """if self.vascular:
            shoot = None
            root = None"""

        """
        Acaulescent – the leaves and inflorescence rise from the ground, and appear to have no stem. They are also known as rosette forms, some of the many conditions that result from very short internodes (i.e. close distances between nodes on the plant stem. See also radical, where leaves arise apparently without stems.
        Acid plant – plants with acid saps, normally due to the production of ammonium salts (malic and oxalic acid)
        Actinomorphic – parts of plants that are radially symmetrical in arrangement.
        Arborescent – growing into a tree-like habit, normally with a single woody stem.
        Ascending – growing uprightly, in an upward direction.
        Assurgent – growth ascending.
        Branching – dividing into multiple smaller segments.
        Caducous – falling away early.
        Caulescent – with a well-developed stem above ground.
        Cespitose – forming dense tufts, normally applied to small plants typically growing into mats, tufts, or clumps.
        Creeping – growing along the ground and producing roots at intervals along the surface.
        Deciduous – falling away after its function is completed.
        Decumbent – growth starts off prostrate and the ends turn upright.
        Deflexed – bending downward.
        Determinate growth – Growing for a limited time, floral formation and leaves (see also Indeterminate).
        Dimorphic – of two different forms.
        Ecad – a plant assumed to be adapted to a specific habitat.
        Ecotone – the boundary that separates two plant communities, generally of major rank – trees in woods and grasses in savanna for example.
        Ectogenesis – variation in plants due to conditions outside of the plants.
        Ectoparasite – a parasitic plant that has most of its mass outside of the host, the body and reproductive organs of the plant live outside of the host.
        Epigeal – living on the surface of the ground. See also terms for seeds.
            Epigean – occurring on the ground.
            Epigeic – plants with stolons on the ground.
            Epigeous – on the ground. Used for leaf fungus that live on the surface of the leaf.
        Epilithic – growing on the surface of rocks.
        Epiphloedal – growing on the bark of trees.
            Epiphloedic – an organism that grows on the bark of trees.
        Epiphyllous – growing on the leaves. For example, Helwingia japonica has epiphyllous flowers (ones that form on the leaves).[5]
        Epiphyte – growing on another organism but not parasitic. Not growing on the ground.
            Epiphytic – having the nature of an epiphyte.
        Equinoctial – a plants that has flowers that open and close at definite times during the day.
        Erect – having an essentially upright vertical habit or position.
        Escape – a plant originally under cultivation that has become wild, a garden plant growing in natural areas.
        Evergreen – remaining green in the winter or during the normal dormancy period for other plants.
        Eupotamous – living in rivers and streams.
        Euryhaline – normally living in salt water but tolerant of variable salinity.
        Eurythermous – tolerant of a wide range of temperatures.
        Exclusive species – confined to specific location.
        Exotic – not native to the area or region.
        Exsiccatus – a dried plant, most often used for specimens in a herbarium.
        Indeterminate growth – Inflorescence and leaves growing for an indeterminate time, until stopped by other factors such as frost (see also Determinate).
        Lax – non upright, growth not strictly upright or hangs down from the point of origin.
        Mallee – a term applied to certain Australian species which grow with multiple stems springing from an underground lignotuber.
        Parasitic – using another plant as a source of nourishment.
        Precocious – flowering before the leaves emerge.
        Procumbent – growing prostrate or trailing, but not rooting at the nodes.
        Prostrate – lying flat on the ground, stems or even flowers in some species.
        Repent – creeping.
        Rosette – cluster of leaves with very short internodes that are crowded together, normally on the surface of the soil but sometimes higher on the stem.
            Rostellate – like a rosette (cf. rostellum).
            Rosulate – arranged into a rosette.
        Runner – an elongated, slender branch that roots at the nodes or tip.
        Stolon – A branch that forms near the base of the plant, grows horizontally, and roots and produces new plants at the nodes or apex.
            Stoloniferous – plants producing stolons.
        Semi-erect – Not growing perfectly straight.
        Suffrutescent – somewhat shrubby, or shrubby at the base.
        Upright – Growing upward.
        Virgate – wand-like, slender erect growing stem with many leaves or very short branches.
        Woody – forming secondary growth laterally around the plant so as to form wood.
        """

        # Duration
        """
        Acme – the time when the plant or population has its maximum vigor.
        Annual – plants that live, reproduce, and die in one growing season.
        Biennial – plants that need two growing seasons to complete their life cycle, normally completing vegetative growth the first year and flowering the second year.
        Herbs – see herbaceous.
        Herbaceous – plants with shoot systems that die back to the ground each year – both annual and non-woody perennial plants.
        Herbaceous perennial – non-woody plants that live for more than two years, with the shoot system dying back to soil level each year.
        Woody perennial – true shrubs and trees, and some vines, with shoot systems that remain alive above the soil level from one year to the next.
        Monocarpic – plants that live for a number of years then, after flowering and seed setting, die.
        """

"""plant = Plant('Plant', True, )
print(plant.name)"""

class Language:
    def __init__(self, name, consonants, vowels, base, words, features={}):
        self.name = name
        # most of this needs to be moved to Features
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
