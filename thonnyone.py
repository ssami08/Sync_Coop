import pygame
import sys
import math  

class Player:
    def __init__(self, x, y, left_key, right_key, jump_key, image_path):
        self.left_key = left_key
        self.right_key = right_key
        self.jump_key = jump_key
        self.velocity_y = 0
        self.gravity = 0.5
        self.speed = 6
        self.on_ground = False
        
        self.ground_platform = None

        self.image = pygame.image.load(image_path).convert_alpha()

                                                    
        bounds = self.image.get_bounding_rect()
        self.image = self.image.subsurface(bounds).copy() # Crop away transparent padding so the rect matches the visible figure

        new_width = int(self.image.get_width() * 0.3)
        new_height = int(self.image.get_height() * 0.3)
        self.image = pygame.transform.smoothscale(self.image, (new_width, new_height))
        self.rect = self.image.get_rect(midbottom=(x, y)) # The rect replaces self.x, self.y and self.ground_y

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == self.jump_key and self.on_ground:
            self.velocity_y = -12

    



    def update(self, keys, platforms):

         # Ride the platform we were standing on last frame
        if self.ground_platform:
            self.rect.x += self.ground_platform.dx
            self.rect.y += self.ground_platform.dy
                
        # Horizontal movement, then fix collisions on x
        dx = 0
        if keys[self.left_key]:
            dx -= self.speed
        if keys[self.right_key]:
            dx += self.speed
        self.rect.x += dx
        for p in platforms:
            if self.rect.colliderect(p.rect):
                if dx > 0:
                    self.rect.right = p.rect.left
                elif dx < 0:
                    self.rect.left = p.rect.right
        
        # Remember where we were before moving vertically
        prev_top = self.rect.top
        prev_bottom = self.rect.bottom
        

        # Vertical movement, then fix collisions on y
        self.velocity_y += self.gravity
        self.rect.y += math.ceil(self.velocity_y)
        self.on_ground = False
        self.ground_platform = None
        
        for p in platforms:
            if not self.rect.colliderect(p.rect):
                continue

            slack = abs(p.dy)                # platform may have moved this frame
            
            if self.velocity_y >= 0 and prev_bottom <= p.rect.top + slack:
                # Feet were above the top: a real landing
                self.rect.bottom = p.rect.top
                self.on_ground = True
                self.ground_platform = p
                self.velocity_y = 0
            elif self.velocity_y < 0 and prev_top >= p.rect.bottom - slack:
                # Head was below the bottom: a real head bonk
                self.rect.top = p.rect.bottom
                self.velocity_y = 0
            else:
                # Overlapping from the side -> push out sideways
                if self.rect.centerx < p.rect.centerx:
                    self.rect.right = p.rect.left
                else:
                    self.rect.left = p.rect.right

        # Keep the player on screen
        self.rect.clamp_ip(pygame.Rect(0, 0, 1280, 720))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        


class Platform:
    def __init__(self, x, y, width, height, color=(90, 96, 120)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.dx = 0
        self.dy = 0
        
    def update(self):
        pass  # static platforms do nothing

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    
class MovingPlatform(Platform):
    def __init__(self, x, y, width, height, end_x, end_y, speed=2):
            super().__init__(x, y, width, height)
            self.start = pygame.math.Vector2(x, y)
            self.end = pygame.math.Vector2(end_x, end_y)
            self.pos = pygame.math.Vector2(x, y)   # float position for smooth movement
            self.target = self.end
            self.speed = speed

    def update(self):
            old_x, old_y = self.rect.topleft

            direction = self.target - self.pos
            if direction.length() <= self.speed:
                # Arrived: snap to the target and turn around
                self.pos = pygame.math.Vector2(self.target)
                self.target = self.start if self.target == self.end else self.end
            else:
                self.pos += direction.normalize() * self.speed

                self.rect.topleft = (round(self.pos.x), round(self.pos.y))

                # Record how far we actually moved, so riders can follow
                self.dx = self.rect.x - old_x
                self.dy = self.rect.y - old_y
    
    
        

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720)) # Set the window size to 1280x720 pixels    
        self.clock = pygame.time.Clock()
        self.players = (Player(150, 400, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, "dude2.png"),
                         Player(450, 400, pygame.K_a, pygame.K_d, pygame.K_w, "dude1.png"))  # Create two players with different controls and images
        self.running = True
        self.platforms = [
        Platform(0, 550, 1280, 170),   
        Platform(300, 430, 200, 20),
        Platform(700, 330, 200, 20),
        MovingPlatform(600, 400, 150, 20, 900, 400),  
        MovingPlatform(1000, 500, 120, 20, 1000, 250, speed=1.5),  
        ]
        
    


    def events_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            for player in self.players:
                player.handle_event(event)  # Handle input events for each player


    def update(self):
        for platform in self.platforms:
            platform.update()

        keys = pygame.key.get_pressed()
        for player in self.players:
            player.update(keys, self.platforms)


    def draw(self):
        self.screen.fill((161, 28, 28))
        for platform in self.platforms: # Draws platforms before drawing players 
            platform.draw(self.screen)
        for player in self.players:
            player.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.events_handler()
            self.update()
            self.draw()
            self.clock.tick(60)


        pygame.quit()
        

pygame.init()


screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Sync- A Co-Op Game")


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
        start_image = pygame.image.load("start.png")
        screen.blit(start_image, (0, 0))
        logo_image = pygame.image.load("start.png")
        mouse=pygame.mouse.get_pos()
        p_bounds = (550,340,140,50)
        o_bounds = (550,420,140,50)
        q_bounds = (550,500,140,50)
        play_button = pygame.draw.rect(screen, RED, p_bounds, 0, 100)
        options_button = pygame.draw.rect(screen, RED, o_bounds, 0, 100)
        quit_button = pygame.draw.rect(screen, RED, q_bounds, 0, 100)
        help_button = pygame.draw.circle(screen, RED, (100,650), 25)


        play_text = font.render("Start", True, WHITE)
        options_text = font.render("Options", True, WHITE)
        quit_text = font.render("Quit", True, WHITE)
        help_text = font.render("?", True, WHITE)


        screen.blit(play_text,(590,350))
        screen.blit(options_text,(575,430))
        screen.blit(quit_text,(590,510))
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
                    help_menu()
                    
                    
                    
        pygame.display.update()


def help_menu():
    help_image = pygame.image.load("help.png")

    while True:
        screen.fill(WHITE)

        screen.blit(help_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        pygame.display.update()

        

start_menu()



    


