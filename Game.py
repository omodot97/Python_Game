#Let’s analyze the provided code. It’s written in **Python** using the **Pygame** library to create a simple 2D game where a red square (the player) can move 
# around a white screen using the W, A, S, D keys.

### Code Analysis
#Here’s a breakdown of what the code does:

#1.Imports and Initialization:
#import pygame` and `import sys`: Imports the Pygame library for game development and the sys module for system operations (like exiting the program).

#pygame.init()`: Initializes Pygame to set up its subsystems (display, sound, etc.).

#2. **Constants**:
#   - `width, height = 800, 600`: Sets the game window size to 800x600 pixels.
#   - `PLAYER_SIZE = 50`: Defines the size of the player (a 50x50 pixel square).
#   - `PLAYER_SPEED = 5`: Sets the player’s movement speed (5 pixels per key press).
#   - `White = (255, 255, 255)` and `Red = (255, 0, 0)`: Defines RGB colors for the background (white) and player (red).

#3. **Game Window Setup**:
#   - `screen = pygame.display.set_mode((width, height))`: Creates an 800x600 pixel game window.

#4. **Player Properties**:
#   - `player_pos = [width // 2, height // 2]`: Places the player at the center of the screen (400, 300) using integer division.

#5. **Game Loop**:
#   - The `while True` loop runs the game continuously until the user quits.
#   - `pygame.event.get()`: Processes events (like closing the window).
#     - If the event is `pygame.QUIT` (e.g., clicking the window’s close button), the game quits using `pygame.quit()` and `sys.exit()`.

#6. **Rendering**:
#   - `screen.fill(White)`: Fills the screen with white to clear the previous frame.
#   - `pygame.draw.rect(screen, Red, (player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE))`: Draws a red square at the player’s current position with the defined size.

#7. **Player Movement**:
#   - `keys = pygame.key.get_pressed()`: Checks the state of all keyboard keys.
#   - The player moves based on key presses:
#     - `W`: Moves up (decreases y-coordinate by `PLAYER_SPEED`).
#     - `S`: Moves down (increases y-coordinate).
#     - `A`: Moves left (decreases x-coordinate).
#     - `D`: Moves right (increases x-coordinate).
#   - Boundary checks ensure the player stays within the screen:
#     - `player_pos[0] = max(0, min(player_pos[0], width - PLAYER_SIZE))`: Keeps the player’s x-coordinate between 0 and `width - PLAYER_SIZE` (750).
#     - `player_pos[1] = max(0, min(player_pos[1], height - PLAYER_SIZE))`: Keeps the player’s y-coordinate between 0 and `height - PLAYER_SIZE` (550).

#8. **Display and Frame Rate**:
#   - `pygame.display.flip()`: Updates the screen to show the new frame.
#   - `pygame.time.Clock().tick(60)`: Caps the frame rate at 60 FPS to ensure smooth and consistent performance.

### Output
#This code doesn’t produce a text-based output like a `print` statement. Instead, it creates a graphical output: a windowed application. Here’s what you’ll see when you run it (assuming Pygame is installed and the code runs without errors):

#- A window (800x600 pixels) with a white background.
#- A red square (50x50 pixels) starting at the center of the screen (position 400, 300).
#- You can move the square using:
#  - **W**: Up
#  - **S**: Down
#  - **A**: Left
#  - **D**: Right
#- The square moves smoothly at 5 pixels per frame, capped at 60 FPS.
#- The square cannot move outside the window boundaries (it’s constrained to stay within 0 to 750 on the x-axis and 0 to 550 on the y-axis).
#- Closing the window (e.g., clicking the “X” button) terminates the program.

### Prerequisites
#To run this code, you need:
#- Python installed (e.g., Python 3.x).
#- Pygame installed (`pip install pygame`).

### Potential Issues
#- If Pygame isn’t installed, you’ll get a `ModuleNotFoundError`.
#- The code assumes a standard keyboard layout with W, A, S, D keys.
#- No error handling is included for display or initialization failures.

#code start

import pygame
import sys
import random

#initialize pygame
pygame.init()

#set up some constants
width, height = 800, 600
PLAYER_SIZE = 50
PLAYER_SPEED = 5
TARGET_SIZE = 20

#create the game window
screen = pygame.display.set_mode((width,height))

#Define some colors
White=(255, 255, 255)
Red=(255, 0, 0)
GREEN=(0, 255, 0)

#player properies
player_pos=[width // 2, height // 2]

#Target properties
target_pos = [random.randint(0, width - TARGET_SIZE), random.randint(0, height - TARGET_SIZE)]

#SCORE PROPERTIES
score = 0
font = pygame.font.Font(None, 36)

#game loop 
while True:
    #handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #define player rectangle for rendering and collision
    player_rect = pygame.Rect(player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE)

    #fill the screen with white 
    screen.fill(White)
    
    #draw the player
    pygame.draw.rect(screen,Red, player_rect)

    #draw the target
    target_rect = pygame.Rect(target_pos[0], target_pos[1], TARGET_SIZE, TARGET_SIZE)
    pygame.draw.circle(screen, GREEN, (target_pos[0] + TARGET_SIZE //2, target_pos[1] + TARGET_SIZE // 2), TARGET_SIZE // 2)

    #update the player position baased on user input
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_w]:
        player_pos[1] -= PLAYER_SPEED
    if keys[pygame.K_s]:
        player_pos[1] += PLAYER_SPEED
    if keys[pygame.K_a]:
        player_pos[0] -= PLAYER_SPEED
    if keys[pygame.K_d]:
        player_pos[0] += PLAYER_SPEED
    if keys[pygame.K_q]:
        player_pos[0] /= PLAYER_SPEED
    if keys[pygame.K_e]:
        player_pos[0] *= PLAYER_SPEED

    #ensure the player doesn't move off the screen
    player_pos[0]=max(0,min(player_pos[0], width-PLAYER_SIZE))
    player_pos[1]=max(0,min(player_pos[1], height-PLAYER_SIZE))

    #CHECK FOR COLLISION WITH TARGET
    target_pos = pygame.Rect(target_pos[0], target_pos[1], TARGET_SIZE, TARGET_SIZE)
    if player_rect.colliderect(target_rect):
        score +=1  # Increment score by 1 (multiplied by 1 effectively adds 1)
        # Spawn new target at random position
        target_pos = [random.randint(0, width - TARGET_SIZE), random.randint(0, height-TARGET_SIZE)]

    #draw the score
    score_text = font.render(f"score: {score}", True, (0, 0, 0)) #black text
    screen.blit(score_text, (10, 10))

    #update the display
    pygame.display.flip()

    #cap the frame rate
    pygame.time.Clock().tick(60)

    