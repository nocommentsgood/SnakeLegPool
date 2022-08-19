import json
from pygame import *
from constants import *
from menu import *
from game import *
from highscore import *

class Control:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        mixer.music.load("sounds/music.mp3")
        mixer.music.play()
        

        
        self.running = True
        self.playing = False

        #initiate key booleans
        self.left_bt, self.right_bt,self.hole1_sensor, self.hole2_sensor, self.hole3_sensor, self.hole4_sensor, self.hole5_sensor, self.hole6_sensor, self.coin_bt, self.enter_bt, self.kill = False, False, False, False, False, False, False, False, False, False, False

        #create surface to draw to
        self.display = pygame.Surface((WIDTH,HEIGHT))
        self.window = pygame.display.set_mode(((WIDTH, HEIGHT)))

        #Create game, end game, and player objects
        self.game = MainDisplay(self)
        self.player = Player(self)
        self.highscore = Highscore(self)
        

        #Create scoring animation objects
        self.holeOne = AnimateHoleOne(self)
        self.holeTwo = AnimateHoleTwo(self)
        self.holeThree = AnimateHoleThree(self)
        self.holeFour = AnimateHoleFour(self)
        self.holeFive = AnimateHoleFive(self)
        self.holeSix = AnimateHoleSix(self)

        #Create menu objects
        self.highscore_menu = HighScoreMenu(self)
        self.rules_menu = RulesMenu(self)
        self.main_menu = MainMenu(self)
        self.curr_menu = self.main_menu

    #Check events loop (Checks if the game has been quit and checks for keyboard input) 
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False

            if event.type == pygame.KEYDOWN:
                self.check_input(event.key)      

    #checks for key and sets its boolean to true
    def check_input(self, key):
        if key == pygame.K_q:
            self.left_bt = True
        if key == pygame.K_w:
            self.right_bt = True
        if key == pygame.K_a:
            self.hole1_sensor = True
        if key == pygame.K_b:
            self.hole2_sensor = True
        if key == pygame.K_c:
            self.hole3_sensor = True
        if key == pygame.K_d:
            self.hole4_sensor = True
        if key == pygame.K_e:
            self.hole5_sensor = True
        if key == pygame.K_f:
            self.hole6_sensor = True
        if key == pygame.K_m:
            self.player.add_credit()
        if key == pygame.K_n:
            self.enter_bt = True
        if key == pygame.K_z:
            pygame.quit()
            sys.exit()
            
    #game_loop controls what state the game is in: menu state, playing state, end state
    def game_loop(self):
        if self.game.end_game_display:
            self.game.display_end_screen()
        if self.game.main_game_display:
            self.game.display_main_screen()
        if self.game.game_animation:
            self.game.hole_animations()


            
    #reset key boolean values
    def reset_keys(self):
        self.left_bt, self.right_bt,self.hole1_sensor, self.hole2_sensor, self.hole3_sensor, self.hole4_sensor, self.hole5_sensor, self.hole6_sensor, self.coin_bt, self.enter_bt, self.kill = False, False, False, False, False, False, False, False, False, False, False

    #draw text method for all classes to use 
    def draw_text(self, text,font_name, size, x, y ):
        font = pygame.font.Font(font_name,size)
        text_surface = font.render(text, True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)


    def handle_highscores(self):
        with open('highscores.txt') as f:
            data = f.read()           
        # reconstructing the data as a dictionary
        self.score_dict = json.loads(data)
        self.dict_names = list(self.score_dict.keys())
        self.dict_values = list(self.score_dict.values())

    def start_playing(self):
        if self.enter_bt:
            if self.player.credits > 0:
                self.player.remove_credit()
                self.game.main_game_display = True
                self.playing = True

    def game_reset(self):
        self.player.total_score = 0
        self.player.shots = 3
        self.playing = False
        self.main_game_display = True
        self.end_game_display = False

    #running loop checcks events and checks if the game is in playing state or menu state
    def run(self):     
        while self.running:
            self.check_events()
            self.start_playing()
            
            if self.playing:
                self.game_loop()               
            else:
                self.curr_menu.display_menu()
            
