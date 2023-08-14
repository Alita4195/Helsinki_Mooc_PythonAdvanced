# Write your solution here
import random


class WordGame:
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds + 1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass  # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) < len(player2_word):
            return 2
        elif len(player2_word) < len(player1_word):
            return 1
        else:
            return "" #super().round_winner(player1_word, player2_word)


class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def count_vowels(self, word: str):
        vowels = "aeiouAEIOU"
        return sum(1 for char in word if char in vowels)

    def round_winner(self, player1_word: str, player2_word: str):
        player1_vowels = self.count_vowels(player1_word)
        player2_vowels = self.count_vowels(player2_word)

        if player1_vowels > player2_vowels:
            return 1
        elif player2_vowels > player1_vowels:
            return 2
        else:
            return "" #super().round_winner(player1_word, player2_word)


class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        valid_moves = ["rock", "paper", "scissors"]

        if player1_word in valid_moves and player2_word in valid_moves:
            if player1_word == "rock" and player2_word == "scissors":
                return 1
            elif player1_word == "paper" and player2_word == "rock":
                return 1
            elif player1_word == "scissors" and player2_word == "paper":
                return 1
            elif player1_word == player2_word:
                return ""#super().round_winner(player1_word, player2_word) # discord:you're choosing a random winner when the result should be a tie
            else:
                return 2  # Player 2 wins

        # If the input from either player is invalid, they lose the round.
        # If both players type in something else than rock, paper or scissors, the result is a tie.
        else:
            if player1_word not in valid_moves and player2_word in valid_moves:
                return 2  # Player 2 wins

            if player1_word in valid_moves and player2_word not in valid_moves:
                return 1  # Player 1 wins
            else:
                return ""  # It's a tie


if __name__ == "__main__":
    p = RockPaperScissors(2)
    p.play()
