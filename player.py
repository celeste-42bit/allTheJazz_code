class Player:
    # CONSTRUCTOR
    # create a player object with all player attributes
    # attributes have to be passed into the constructor at character creation
    def __init__(self, name, surname, gender, pronoun, clan, ventrue_title, story_title, story_achievements, allies, gang, resources, control, STR, DEX, STA, CHA, MAN, COM, INT, WIT, RES, ATHL, CLND, COMB, SURV, INST, INTN, LEAD, PERS, SUBT, AWRN, OCLT, SCIE, INVS, dominate, presence, celerity, auspex, fortitude, thaumaturgy, dmgtaken, wpexpended, save):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.pronoun = pronoun
        self.clan = clan
        self.ventrue_title = ventrue_title
        self.story_title = story_title

        self.story_achievements = story_achievements
        self.allies = allies
        self.gang = gang
        self.resources = resources
        self.control = control

        self.STR = STR
        self.DEX = DEX
        self.STA = STA
        self.CHA = CHA
        self.MAN = MAN
        self.COM = COM
        self.INT = INT
        self.WIT = WIT
        self.RES = RES

        self.ATHL = ATHL
        self.CLND = CLND
        self.COMB = COMB
        self.SURV = SURV
        self.INST = INST
        self.INTN = INTN
        self.LEAD = LEAD
        self.PERS = PERS
        self.SUBT = SUBT
        self.AWRN = AWRN
        self.OCLT = OCLT
        self.SCIE = SCIE
        self.INVS = INVS

        self.dominate = dominate
        self.presence = presence
        self.celerity = celerity
        self.auspex = auspex
        self.fortitude = fortitude
        self.thaumaturgy = thaumaturgy

        # health and willpower don't need to be passed, bc they are calculated!
        self.dmgtaken = dmgtaken
        self.wpexpended = wpexpended

        self.save = save  # the last name of the text file the player saved in!

    # functions

    def createenv(self):
        print("Created new character.env")
        # copy character_template.env as character.env
        # set all null values to None
        # return

    def calculate_hpwp(self):  # returns willpower and health
        health = self.STA + 3 - self.dmgtaken
        willpower = self.COM + self.RES - self.wpexpended
        # implement save to .env
        return health & willpower

    def save_dotenv(self):
        print("saved!")

        # write to character.env