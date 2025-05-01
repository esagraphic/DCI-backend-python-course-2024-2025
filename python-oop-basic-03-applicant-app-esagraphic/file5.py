import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Dice Game')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Load dice images
dice_images = [
    pygame.image.load(f'dice{i}.png') for i in range(1, 7)
]

# Game variables
dice = None
player1_name = ''
player2_name = ''
player1_score = 0
player2_score = 0
rounds = 5
round_number = 1
game_started = False

# Input box settings
input_box1 = pygame.Rect(100, 100, 140, 32)
input_box2 = pygame.Rect(100, 150, 140, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
active1 = False
active2 = False
text1 = ''
text2 = ''
play_button = pygame.Rect(100, 200, 100, 50)

def roll_dice():
    """Rolls the dice and returns a random number between 1 and 6."""
    return random.randint(1, 6)

def draw_text(text, font, color, surface, x, y):
    """Helper function to draw text on the screen."""
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Main loop
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if play button was clicked
            if play_button.collidepoint(event.pos):
                if text1 != '' and text2 != '':
                    player1_name = text1
                    player2_name = text2
                    game_started = True
                    round_number = 1
                    player1_score = 0
                    player2_score = 0
                    print(f"Starting game with {player1_name} and {player2_name}")
            
            # Check if text boxes were clicked
            if input_box1.collidepoint(event.pos):
                active1 = not active1
            else:
                active1 = False
            if input_box2.collidepoint(event.pos):
                active2 = not active2
            else:
                active2 = False

        if event.type == pygame.KEYDOWN:
            if active1:
                if event.key == pygame.K_RETURN:
                    active1 = False
                elif event.key == pygame.K_BACKSPACE:
                    text1 = text1[:-1]
                else:
                    text1 += event.unicode
            if active2:
                if event.key == pygame.K_RETURN:
                    active2 = False
                elif event.key == pygame.K_BACKSPACE:
                    text2 = text2[:-1]
                else:
                    text2 += event.unicode

    # Render the input boxes
    color1 = color_active if active1 else color_inactive
    color2 = color_active if active2 else color_inactive
    pygame.draw.rect(screen, color1, input_box1, 2)
    pygame.draw.rect(screen, color2, input_box2, 2)
    
    draw_text(text1, font, BLACK, screen, input_box1.x+5, input_box1.y+5)
    draw_text(text2, font, BLACK, screen, input_box2.x+5, input_box2.y+5)
    
    # Display text on buttons
    draw_text("Player 1 Name:", font, BLACK, screen, 100, 70)
    draw_text("Player 2 Name:", font, BLACK, screen, 100, 120)
    pygame.draw.rect(screen, GREEN, play_button)
    draw_text("Play", font, BLACK, screen, play_button.x+25, play_button.y+10)
    
    if game_started:
        # Play the game and display dice images
        if round_number <= rounds:
            # Roll dice for both players
            p1_roll = roll_dice()
            p2_roll = roll_dice()
            player1_score += p1_roll
            player2_score += p2_roll
            print(f"Round {round_number}: {player1_name} rolled {p1_roll}, {player2_name} rolled {p2_roll}")

            # Display dice images
            screen.blit(dice_images[p1_roll - 1], (400, 100))  # Player 1 dice
            screen.blit(dice_images[p2_roll - 1], (400, 200))  # Player 2 dice

            draw_text(f"Round {round_number}: {player1_name} rolled {p1_roll}, {player2_name} rolled {p2_roll}", font, BLACK, screen, 100, 300)
            round_number += 1

        else:
            game_started = False
            # Determine and display winner
            winner = player1_name if player1_score > player2_score else player2_name
            draw_text(f"Game Over! {winner} wins!", font, RED, screen, 100, 400)

    pygame.display.flip()

pygame.quit()
