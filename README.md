# BYU Flappy Bird

A Python-based recreation of the classic Flappy Bird game with a BYU theme. Players control Cosmo the Cougar, navigating through obstacles while avoiding collisions with pipes and the ground.

The project was developed as a personal programming project to explore game development concepts and gain hands-on experience with Python and Pygame.

## Overview

The game features:
- Custom BYU-themed graphics and game assets.
- Player movement with gravity-based physics and keyboard-controlled jumping.
- Randomized obstacle generation.
- Collision detection between the player, obstacles, and environment.
- A scoring system that tracks successfully passed obstacles.
- A start menu and game-over screen.

## Technologies

- Python
- Pygame

## Controls

| Key | Action |
|---|---|
| `SPACE` | Start the game / Make Cosmo jump |
| `R` | Restart after a game over |

## Installation and Execution

### Requirements

- Python 3.x
- Pygame

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
   ```

2. Navigate to the project directory:

   ```bash
   cd YOUR-REPOSITORY
   ```

3. Install the required dependency:

   ```bash
   pip install pygame
   ```

4. Start the game:

   ```bash
   python main.py
   ```

## Project Structure

```
BYU-Flappy-Bird/
├── images/
│   ├── cosmo.png
│   ├── stadium2.png
│   ├── ground1.png
│   ├── pipe_top.png
│   ├── pipe_bottom.png
│   ├── start2.png
│   └── game_over.png
├── main.py
└── README.md
```

## Technical Concepts

This project incorporates several fundamental programming and game development concepts:

- **Object-Oriented Programming:** Implemented separate classes for the player, obstacles, and ground elements.
- **Game Loop Management:** Used a continuous game loop to process input, update game objects, and render each frame.
- **Collision Detection:** Used Pygame sprite collision functionality to detect interactions between game objects.
- **Basic Physics:** Implemented gravity, velocity, and keyboard-controlled upward movement.
- **Randomized Generation:** Generated obstacles at varying vertical positions and intervals to create dynamic gameplay.
- **Sprite Management:** Used Pygame sprite groups to organize and manage game objects.

## Project Background

This project was developed independently as an opportunity to experiment with Python game development and apply programming fundamentals in a practical setting. It was inspired by the original Flappy Bird game and adapted with BYU-themed graphics and characters.
