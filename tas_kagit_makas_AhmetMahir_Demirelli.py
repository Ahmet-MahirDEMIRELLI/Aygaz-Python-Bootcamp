# On terminal -> python tas_kagit_makas_AhmetMahir_Demirelli.py
# Images are necessary

import tkinter as tk
from PIL import Image, ImageTk
import webbrowser
import random

player_game_score = 0
computer_game_score = 0


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    window.geometry(f"{width}x{height}+{x}+{y}")


def tas_kagit_makas_AhmetMahir_Demirelli():
    introduction_window = tk.Tk()
    introduction_window.title("Rock, Paper, Scissors, Lizard, Spock")

    center_window(introduction_window, 1200, 800)

    rules_image = Image.open("images/rule-book.png")
    rules_photo = ImageTk.PhotoImage(rules_image)

    img_label = tk.Label(introduction_window, image=rules_photo)
    img_label.pack(pady=20)

    url = "https://www.youtube.com/watch?v=pIpmITBocfM#:~:"
    url_label = tk.Label(introduction_window, text="Click for Sheldon",
                         fg="blue", cursor="hand2", font=("Arial", 12))
    url_label.pack(pady=10)

    def open_url(event):
        webbrowser.open_new(url)

    url_label.bind("<Button-1>", open_url)

    start_label = tk.Label(introduction_window, text="First one to win two rounds wins the game.\nAfter that you can "
                                                     "either want to play again or exit.", font=("Arial", 20))
    start_label.pack(pady=10)

    def start_game():
        introduction_window.destroy()
        show_start_screen()

    start_button = tk.Button(introduction_window, text="I understand the rules.",
                             font=("Arial", 15), command=start_game)
    start_button.pack(pady=20)

    introduction_window.mainloop()


def show_start_screen():
    start_window = tk.Tk()
    start_window.title("Rock, Paper, Scissors, Lizard, Spock")
    center_window(start_window, 1200, 800)

    computer_image = Image.open("images/sheldon.png")
    computer_photo = ImageTk.PhotoImage(computer_image)
    img_label = tk.Label(start_window, image=computer_photo)
    img_label.pack(pady=20)

    def go_to_game_screen():
        start_window.destroy()
        show_game_screen()

    challenge_button = tk.Button(start_window, text="Challenge The Master", font=("Arial", 15),
                                 command=go_to_game_screen)
    challenge_button.pack(pady=20)

    start_window.mainloop()


def show_game_screen():
    global player_game_score, computer_game_score
    player_round_score = 0
    computer_round_score = 0

    def make_choice(user_choice):
        nonlocal player_round_score, computer_round_score
        global player_game_score, computer_game_score

        computer_choice = random.choice(choices)
        parts = determine_winner(user_choice, computer_choice).split(',')
        if parts[0] == "0":
            computer_round_score += 1
            computer_round_label.config(text=f"[{computer_round_score}]")
            result_label.config(text=f"Computers {computer_choice} {parts[1]} your {user_choice}.")
        elif parts[0] == "1":
            player_round_score += 1
            player_round_label.config(text=f"[{player_round_score}]")
            result_label.config(text=f"Your {user_choice} {parts[1]} computers {computer_choice}.")
        else:  # Tie
            result_label.config(text=f"Your {user_choice} tied with computers {computer_choice}.")

        if player_round_score >= 2 or computer_round_score >= 2:
            bottom_frame.forget()
            game_window.after(1500, lambda: [game_window.destroy(), show_winner_screen()])

    def determine_winner(user_choice, computer_choice):
        winning_combinations = {
            ('rock', 'scissors'): "crushed ",
            ('rock', 'lizard'): "crushed ",
            ('scissors', 'paper'): "cut",
            ('scissors', 'lizard'): "decapitated",
            ('paper', 'rock'): "covered",
            ('paper', 'spock'): "disproved",
            ('lizard', 'spock'): "poisoned",
            ('lizard', 'paper'): "ate",
            ('spock', 'scissors'): "smashed",
            ('spock', 'rock'): "vaporized",
        }

        if user_choice == computer_choice:
            return "It's a Tie!"

        if (user_choice, computer_choice) in winning_combinations:
            return "1," + winning_combinations[(user_choice, computer_choice)]
        else:
            return "0," + winning_combinations[(computer_choice, user_choice)]

    def select_choice(choice):
        make_choice(choice)

    def show_winner_screen():
        nonlocal player_round_score, computer_round_score
        global player_game_score, computer_game_score

        winner_window = tk.Tk()
        winner_window.title("Game Over")
        center_window(winner_window, 600, 300)

        if player_round_score >= 2:
            message = f"Congratulations! You won the game {player_round_score} to {computer_round_score}."
            player_game_score += 1
        else:
            message = f"Sorry, you lost the game {player_round_score} to {computer_round_score}."
            computer_game_score += 1

        player_round_score = 0
        computer_round_score = 0
        result_label = tk.Label(winner_window, text=message, font=("Arial", 16))
        result_label.pack(pady=20)

        def exit_game():
            winner_window.destroy()
            print("Thanks for playing!")

        def new_game():
            winner_window.destroy()
            show_game_screen()

        def get_computer_choice():
            global player_game_score, computer_game_score

            if computer_game_score <= player_game_score:
                return "Play Again" if random.random() < 0.5 else "Don't Play"
            elif computer_game_score >= 2 * player_game_score:
                return "Play Again" if random.random() < 0.75 else "Don't Play"
            else:  # computer_game_score > player_game_score:
                return "Play Again" if random.random() < 0.66 else "Don't Play"

        if get_computer_choice() == "Play Again":
            new_game_button = tk.Button(winner_window, text="Play Again", command=new_game, font=("Arial", 15))
            new_game_button.pack(pady=10)

            exit_button = tk.Button(winner_window, text="Exit", command=exit_game, font=("Arial", 15))
            exit_button.pack(pady=10)
        else:
            no_play_message = tk.Label(winner_window, text="Computer didn't want to play again", font=("Arial", 12),
                                       fg="red")
            no_play_message.pack(pady=10)

            score_summary = tk.Label(winner_window, text=f"Overall Score\nComputer: {computer_game_score}  "
                                                         f"Player: {player_game_score}", font=("Arial", 12), fg="black")
            score_summary.pack(pady=10)

            exit_button = tk.Button(winner_window, text="Exit", command=exit_game, font=("Arial", 15))
            exit_button.pack(pady=10)

        winner_window.mainloop()

    game_window = tk.Tk()
    game_window.title("Rock, Paper, Scissors, Lizard, Spock")
    center_window(game_window, 1200, 800)

    top_frame = tk.Frame(game_window)
    top_frame.pack(side=tk.TOP, fill=tk.X)

    player_score_label = tk.Label(top_frame, text=f"Player Score: {player_game_score}", font=("Arial", 15))
    player_score_label.pack(side=tk.RIGHT, padx=20, pady=20)
    player_round_label = tk.Label(top_frame, text=f"[{player_round_score}]", font=("Arial", 15))
    player_round_label.pack(side=tk.RIGHT, padx=20, pady=20)

    computer_score_label = tk.Label(top_frame, text=f"Computer Score: {computer_game_score}", font=("Arial", 15))
    computer_score_label.pack(side=tk.LEFT, padx=20, pady=20)
    computer_round_label = tk.Label(top_frame, text=f"[{computer_round_score}]", font=("Arial", 15))
    computer_round_label.pack(side=tk.LEFT, padx=20, pady=20)

    result_label = tk.Label(game_window, text="", font=("Arial", 20))
    result_label.pack(pady=20)

    choices = ["rock", "paper", "scissors", "lizard", "spock"]

    bottom_frame = tk.Frame(game_window)
    bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=20)

    for choice in choices:
        photo = ImageTk.PhotoImage(Image.open(f"images/{choice}.png"))
        button = tk.Button(bottom_frame, image=photo, command=lambda c=choice: select_choice(c))
        button.image = photo
        button.pack(side=tk.LEFT, expand=True, padx=10)

    game_window.mainloop()


tas_kagit_makas_AhmetMahir_Demirelli()
