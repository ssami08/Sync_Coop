import pygame

class Player:
    def __init__(self, x, y): # Initialize the player with position, y-velocity, gravity, speed, radius, and ground level
        self.x = x
        self.y = y
        self.velocity_y = 0
        self.gravity = 0.5
        self.speed = 10
        self.ground_y = 360
        self.image = pygame.image.load("dude2.png")
        new_width = int(self.image.get_width() * 0.5)
        new_height = int(self.image.get_height() * 0.5)
        self.image = pygame.transform.smoothscale(self.image, (new_width, new_height))
       


    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return


        if event.key == pygame.K_RIGHT:
            self.x += self.speed
        elif event.key == pygame.K_LEFT:
            self.x -= self.speed
        elif event.key == pygame.K_DOWN:
            self.y += self.speed


    def update(self): # Update the player's position based on gravity and ensure they don't fall below the ground level
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
        self.screen = pygame.display.set_mode((600, 400)) # Set the window size to 640x480 pixels    
        self.clock = pygame.time.Clock()
        self.player = Player(150, 360)
        self.running = True


    def events_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.player.handle_event(event)


    def update(self):
        self.player.update()  # Update the player position based on gravity and input


    def draw(self):
        self.screen.fill((20, 24, 40))
        pygame.draw.line(self.screen, (90, 96, 120), (0, 360), (600, 360), 3)
        self.player.draw(self.screen) # Draw the player on the screen
        pygame.display.flip() # Update the display to show the new frame


    def run(self):
        while self.running:
            self.events_handler()
            self.update()
            self.draw()
            self.clock.tick(60)


        pygame.quit()




if __name__ == "__main__": # Run the game if this file is executed directly
    Game().run()
