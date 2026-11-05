import pygame
from sys import exit
import random

pygame.init()
clock = pygame.time.Clock()

game_height = 640
game_width = 470
window = pygame.display.set_mode((game_width,game_height))

cosmo_image = pygame.image.load("images/cosmo.png")
stadium_image = pygame.image.load("images/stadium2.png")
ground_image = pygame.image.load("images/ground1.png")
pipe_top_image = pygame.image.load("images/pipe_top.png")
pipe_bottom_image = pygame.image.load("images/pipe_bottom.png")
start_image = pygame.image.load("images/start2.png")
game_over_image = pygame.image.load("images/game_over.png")

scroll_speed = 2
cosmo_start_position = (100, 270)
score = 0
font = pygame.font.SysFont('Segoe', 30)
game_stopped = True

class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.x <= - game_width:
            self.kill()

class Cosmo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cosmo_image
        self.rect = self.image.get_rect()
        self.rect.center = cosmo_start_position
        self.vel = 0
        self.flap = False
        self.alive = True

    def update(self, user_input):
        self.vel += 0.5
        if self.vel > 7:
            self.vel = 7
        if self.rect.y < 545:
            self.rect.y += int(self.vel)
        if self.vel == 0:
            self.flap = False

        if user_input[pygame.K_SPACE] and not self.flap and self.rect.y > 0 and self.alive:
            self.flap = True
            self.vel = -7

class Pipes(pygame.sprite.Sprite):
    def __init__(self, x, y, image, pipe_type):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.enter = False
        self.exit = False
        self.passed = False
        self.pipe_type = pipe_type

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.x <= - game_width:
            self.kill()

        global score
        if self.pipe_type == 'bottom':
            if cosmo_start_position[0] > self.rect.topleft[0] and not self.passed:
                self.enter = True
            if cosmo_start_position[0] > self.rect.topright[0] and not self.passed:
                self.exit = True
            if self.enter and self.exit and not self.passed:
                self.passed = True
                score += 1


def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def main():
    global score
    #Cosmo
    cosmo = pygame.sprite.GroupSingle()
    cosmo.add(Cosmo())

    #Pipes
    pipe_timer = 0
    pipes = pygame.sprite.Group()

    #Ground
    ground_x =0
    ground_y = 564
    ground = pygame.sprite.Group()
    ground.add(Ground(ground_x, ground_y))


    run = True
    while run:
        quit_game()
        #Reset Frame
        window.fill((0,0,0))
        #User input
        user_input = pygame.key.get_pressed()
        #Draw Background
        window.blit(stadium_image, (0,0))
        #Infinite Ground
        if len(ground) <= 2:
            ground.add(Ground(game_width, ground_y))
        #Draw objects
        ground.draw(window)
        cosmo.draw(window)
        pipes.draw(window)

        # # Debug: Draw Hitboxes
        # for pipe in pipes:
        #     pygame.draw.rect(window, (255, 0, 0), pipe.rect, 2)  # Red box for pipes
        #
        # pygame.draw.rect(window, (0, 255, 0), cosmo.sprite.rect, 2)  # Green box for Cosmo

        # Show Score
        score_text = font.render('Score: ' + str(score), True, pygame.Color(255, 255, 255))
        window.blit(score_text, (20, 20))

        #Update objects
        if cosmo.sprite.alive:
            ground.update()
            pipes.update()
        cosmo.update(user_input)

        # Collision Detection
        collision_pipes = pygame.sprite.spritecollide(cosmo.sprites()[0], pipes, False)
        collision_ground = pygame.sprite.spritecollide(cosmo.sprites()[0], ground, False)
        if collision_pipes or collision_ground:
            cosmo.sprite.alive = False
            if collision_ground:
                window.blit(game_over_image, (game_width // 2 - game_over_image.get_width() // 2,
                                              game_height // 2 - game_over_image.get_height() // 2))
                if user_input[pygame.K_r]:
                    score = 0
                    break

        #Spawn Pipes
        if pipe_timer <= 0 and cosmo.sprite.alive:
            x_top = 550
            x_bottom = 550
            y_top = random.randint(-600, -480)
            y_bottom = y_top + random.randint(110, 140) + pipe_bottom_image.get_height()
            pipes.add(Pipes(x_top, y_top, pipe_top_image, 'top'))
            pipes.add(Pipes(x_bottom, y_bottom, pipe_bottom_image, 'bottom'))
            pipe_timer = random.randint(120, 180)
        pipe_timer -= 1.5

        clock.tick(60)
        pygame.display.update()

# Menu
def menu():
    global game_stopped

    while game_stopped:
        quit_game()

        # Draw Menu
        window.fill((0, 0, 0))
        window.blit(stadium_image, (0, 0))
        window.blit(ground_image, Ground(0, 564))
        window.blit(cosmo_image, (100, 250))
        window.blit(start_image, (game_width // 2 - start_image.get_width() // 2,
                                  game_height // 2 - start_image.get_height() // 2))

        # User Input
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_SPACE]:
            main()

        pygame.display.update()


menu()