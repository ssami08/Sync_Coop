# Sync

## A Co-operative Platformer

**Sync** is a 2D cooperative puzzle platformer developed as part of my OCR A Level Computer Science NEA.

The game is designed around two players working together to solve puzzles, navigate environments and reach their respective exits. The main aim is to create a game where cooperation is essential rather than simply allowing two players to play alongside each other.

The project is being developed in **Python** using the **PyGame** library. The game focuses primarily on local multiplayer, with both players sharing the same computer and interacting with the same game world.

## Features

### Co-operative Gameplay

Both players need to work together to progress through the levels. Puzzles are designed so that one player can interact with the environment to help the other player progress.

### Player Movement

Both players have their own controls and can:

* Move left and right
* Jump
* Crouch
* Sprint
* Interact with objects

The game is designed to respond to simultaneous inputs from both players.

### Puzzle Mechanics

Levels contain interactive objects such as:

* Buttons
* Levers
* Moving platforms
* Rotating platforms
* Exit doors
* Environmental triggers

These mechanics are combined to create increasingly challenging puzzles.

### Enemy Turrets

Some levels contain turrets which track and target players.

Turrets can calculate the distance to each player and target the closer player. They can also fire projectiles which move through the level and cause damage when they collide with a player.

### Health and Respawning

Players have health which is continuously updated during gameplay.

If a player dies, they can respawn after a delay rather than being permanently eliminated. If both players die, the level is reset. This keeps both players involved throughout the level.

### Progress Tracking

The game is designed to track information such as:

* Level progress
* Completion time
* Number of deaths
* Personal best times

This information can be displayed to the player between levels.

## Controls

### Player 1

| Action     | Key |
| ---------- | --- |
| Move Left  | A   |
| Move Right | D   |
| Jump       | W   |
| Crouch     | S   |

### Player 2

| Action     | Key         |
| ---------- | ----------- |
| Move Left  | Left Arrow  |
| Move Right | Right Arrow |
| Jump       | Up Arrow    |
| Crouch     | Down Arrow  |

Both players use the same keyboard, allowing the game to be played locally on one computer.

## Technology

**Language:** Python

**Library:** PyGame

**Platform:** PC

**Multiplayer:** Local co-op

The project uses PyGame because it provides the functionality required to create the game's graphics, input handling, collision detection and game loop while remaining suitable for the scope of the project.
