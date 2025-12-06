# Guess the Number – CLI Game (Python)

A simple command-line **“guess the number”** game written in Python.

I built this as one of my very first programming projects to practice:

- basic Python syntax and control flow,
- functions and code organization,
- input validation and error handling,
- saving player statistics to a file.

I used an AI assistant (ChatGPT) to help me understand concepts, debug errors, and refactor the code, but the logic and structure are things I worked through myself step by step.

---

## Game Description

The game:

1. Asks for the **player’s name**.
2. Asks the player to choose a **difficulty**:
   - `1` – Easy: number between 1–10, 5 attempts
   - `2` – Medium: number between 1–20, 4 attempts
   - `3` – Hard: number between 1–50, 3 attempts
3. Picks a **secret random number** in the chosen range.
4. Lets the player guess, with:
   - feedback: `too high` / `too low` / `correct`
   - a limited number of attempts
5. After each game, it updates and shows the player’s:
   - total **wins**
   - total **losses**

Player stats are stored in a simple `scores.txt` file so they persist between runs.

---

## Main Features

- **Multiple difficulty levels**
  - Different number ranges and attempts per difficulty.

- **Input validation**
  - Difficulty must be `1`, `2` or `3`.
  - Guess must be a number within the allowed range.
  - If the player types something invalid (e.g. `"abc"`), the game asks again instead of crashing.

- **Per-player statistics**
  - When you enter your name, the game:
    - loads your past stats from `scores.txt` (if present),
    - or creates a new record if you’re a new player.
  - After each game, it updates:
    - `wins`
    - `losses`

- **Play again loop**
  - At the end of each round you can choose:
    - `yes` – play another round
    - `no` – exit the game

---

## Project Structure

Typical structure of the CLI project:

```text
guessnumber_cli/
├─ guess_number.py    # main Python script (CLI game)
└─ scores.txt         # created/updated at runtime to store stats
