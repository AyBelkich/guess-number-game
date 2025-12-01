import random

def choose_difficulty():
    print("Choose game difficulty:")
    print("1. Easy = 1-10")
    print("2. Medium = 1-20")
    print("3. Hard = 1-50")

    difficulty = input("Enter 1, 2 or 3: ")

    while difficulty not in ("1", "2", "3"):
        difficulty = input("Invalid response, please select 1, 2 or 3: ")

    if difficulty == "1":
        return 10, 5
    elif difficulty == "2":
        return 20, 4
    else:
        return 50, 3
    
def get_valid_guess(number_range):
    while True:
        player_guess = input("Guess: ")
        
        try:
            guess = int(player_guess)
        except ValueError:
            print("Invalid response. Please re-enter a valid number.")
            continue

        if 1 <= guess <= number_range:
            return guess
        else:
            print("Invalid response. Please re-enter a number between 1 and %d" % number_range)

def play_round():
    #DIFFICULTY FUNCTION
    number_range, max_attempts = choose_difficulty()


    print("I'm thinking of a number between 1 and %d..." % number_range)

    secret_number = random.randint(1, number_range)
    attempts_used = 0

    print("I'll give you a guess...")

    while attempts_used < max_attempts:

        #GUESS VALIDATION
        guess = get_valid_guess(number_range)

        attempts_used +=1

        if guess > secret_number:
            print("Oops, you're a little too high")
        elif guess < secret_number:
            print("Oops, you're a little too low")
        else:
            print("WIN")
            return "WIN"

        print("Attempts used: %d/%d" %(attempts_used, max_attempts))
        
    if attempts_used == max_attempts and guess != secret_number:
        print("😢 You're out of attempts. The number was", secret_number)
        return "LOSE"

def load_stats():
    stats = {}
    
    try:
        with open("scores.txt", "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                name, wins_str, losses_str = line.split(";")
    
                stats[name] = {
                    "wins": int(wins_str),
                    "losses": int(losses_str)
                }
    except FileNotFoundError:
        pass

    return stats

def save_stats(stats):
    with open("scores.txt", "w") as f:
        for name, record in stats.items():
            wins = record["wins"]
            losses = record["losses"]
            line = "%s;%d;%d\n" % (name, wins, losses)
            f.write(line)

def main():
    play_again = "yes"
    stats = load_stats()

    print("Welcome to the game.")
    player_name = input("What is your name? ")
    print("Nice to meet you %s !" % player_name)

    if player_name not in stats:
        stats[player_name] = {"wins": 0, "losses": 0}
    
    while play_again.lower() == "yes":

        result = play_round()

        if result == "WIN":
            stats[player_name]["wins"] += 1
        else:
            stats[player_name]["losses"] += 1
        
        wins = stats[player_name]["wins"]
        losses = stats[player_name]["losses"]

        print("You", result)
        print("Current score for %s: %d wins, %d losses" % (player_name, wins, losses))

        play_again = input("Do you want to play again? ")

        while play_again.lower() not in ("yes", "no"):
            play_again = input("Please type 'yes' or 'no': ")

    save_stats(stats)
    
    wins = stats[player_name]["wins"]
    losses = stats[player_name]["losses"]
    print("Final score for %s: %d wins, %d losses" % (player_name, wins, losses))
    print("Thanks for playing! Goodbye.")

main()
