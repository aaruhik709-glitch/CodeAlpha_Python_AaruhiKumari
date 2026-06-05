import random

# List of predefined words
words = ["python", "apple", "coding", "laptop", "camera"]

# Randomly choose a word
secret_word = random.choice(words)

# Create blanks
guessed_word = ["_"] * len(secret_word)

# Attempts allowed
attempts = 6

# Store guessed letters
guessed_letters = []

print("🎮 Welcome to Hangman Game")
print("Guess the word one letter at a time!")

# Game loop
while attempts > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Attempts Left:", attempts)
    print("Guessed Letters:", guessed_letters)

    # Take input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter only one alphabet.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    # Add guessed letter
    guessed_letters.append(guess)

    # Check if letter exists
    if guess in secret_word:
        print("✅ Correct Guess!")

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess

    else:
        print("❌ Wrong Guess!")
        attempts -= 1

# Final result
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("\n💀 Game Over! The word was:", secret_word)
