import pygame
import sys



class Player:
    def __init__(self, x, y, left_key, right_key, jump_key,image_path): # Initialize the player with position, y-velocity, gravity, speed, radius, and ground level
        self.x = x
        self.y = y
        self.left_key = left_key
        self.right_key = right_key
        self.jump_key = jump_key
        self.velocity_y = 0
        self.gravity = 0.5
        self.speed = 10
        self.ground_y = y
        self.image = pygame.image.load(image_path)
        new_width = int(self.image.get_width() * 0.5)
        new_height = int(self.image.get_height() * 0.5)
        self.image = pygame.transform.smoothscale(self.image, (new_width, new_height))
       


    def handle_event(self, event):
        if (event.type == pygame.KEYDOWN and event.key == self.jump_key and self.y >= self.ground_y):
            self.velocity_y = -12


        
    def update(self,keys): # Update the player's position based on gravity and ensure they don't fall below the ground level
        if keys[self.left_key]:
            self.x -= self.speed
        if keys[self.right_key]:
            self.x += self.speed
        self.velocity_y += self.gravity
        self.y += self.velocity_y
        if self.y >= self.ground_y:
            self.y = self.ground_y
            self.velocity_y = 0


    def draw(self, screen):
        image_rect = self.image.get_rect(
            center=(int(self.x), int(self.y)))
        screen.blit(self.image, image_rect)




class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720)) # Set the window size to 1280x720 pixels    
        self.clock = pygame.time.Clock()
        self.players = (Player(150, 500, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, "dude2.png"),
                         Player(450, 500, pygame.K_a, pygame.K_d, pygame.K_w, "dude1.png"))  # Create two players with different controls and images
        self.running = True


    def events_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            for player in self.players:
                player.handle_event(event)  # Handle input events for each player


    def update(self):
        keys = pygame.key.get_pressed()
        for player in self.players:
            player.update(keys)  # Update each player's position based on gravity and input


    def draw(self):
        self.screen.fill((161,28, 28)) 
        pygame.draw.line(self.screen, (90, 96, 120), (0, 550), (1280, 550), 3)
        for player in self.players:
            player.draw(self.screen)  # Draw each player on the screen
        pygame.display.flip()  # Update the display to show the new frame


    def run(self):
        while self.running:
            self.events_handler()
            self.update()
            self.draw()
            self.clock.tick(60)


        pygame.quit()
        

pygame.init()


screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Start Menu - Sync")


WHITE = (255,255,255)
LIGHT = (170,170,170)
DARK = (100,100,100)
RED = (162,24,32)


font = pygame.font.SysFont("Helvetica Bold", 35)


def start():
    while True :
        for event in pygame.event.get():
            if event.type == "quit" :
                pygame.quit()
                sys.exit()
        Game().run()
        

    
        


def start_menu() :
    while True:
        screen.fill(WHITE)
        mouse=pygame.mouse.get_pos()
        p_bounds = (550,300,140,50)
        o_bounds = (550,380,140,50)
        q_bounds = (550,460,140,50)
        play_button = pygame.draw.rect(screen, RED, p_bounds, 0, 100)
        options_button = pygame.draw.rect(screen, RED, o_bounds, 0, 100)
        quit_button = pygame.draw.rect(screen, RED, q_bounds, 0, 100)
        help_button = pygame.draw.circle(screen, RED, (100,650), 25)


        play_text = font.render("Start", True, WHITE)
        options_text = font.render("Options", True, WHITE)
        quit_text = font.render("Quit", True, WHITE)
        help_text = font.render("?", True, WHITE)


        screen.blit(play_text,(590,310))
        screen.blit(options_text,(575,390))
        screen.blit(quit_text,(590,470))
        screen.blit(help_text,(95,640))


        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            if event.type == pygame.MOUSEBUTTONDOWN:


                if play_button.collidepoint(mouse):
                    start()


                if quit_button.collidepoint(mouse):
                    pygame.quit()
                    sys.exit()
                    
                if help_button.collidepoint(mouse):
                    
                    pygame.image.load("helpscreen")
                    
                    
                    
                    
                    
        pygame.display.update()


start_menu()



    

