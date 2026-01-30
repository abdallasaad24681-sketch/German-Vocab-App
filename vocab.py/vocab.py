import random

words_dict = {}
name = input("Enter your name: ")

try:
    with open("dictionary.txt", "r", encoding="utf-8") as file:
        for line in file:
            if ":" in line:
                key, value = line.strip().split(":")
                words_dict[key] = value
    print(f"Perfect ✅ {name}! {len(words_dict)} words loaded from your dictionary.")
except FileNotFoundError:
    print(f"Perfect ✅ {name}! Starting a new dictionary.")

while True:
    print("\n" + "=" * 40)
    action = input("Type (add), (test), (show), (search), or (exit) to quit: ").lower()

    if action == 'exit':
        print(f"👋 Goodbye {name.upper()}! Keep practicing.")
        break

    elif action == 'add':
        word = input("Enter German word: ")
        meaning = input("Enter meaning (English/Arabic): ")
        words_dict[word] = meaning

        with open("dictionary.txt", "a", encoding="utf-8") as file:
            file.write(f"{word}:{meaning}\n")

        count = len(words_dict)
        if count < 5:
            rank = "Beginner 🌱"
        elif count < 15:
            rank = "Student 📚"
        else:
            rank = "German Legend 🏆"

        print(f"Saved! Current Rank: {rank}")

    elif action == 'show':
        if not words_dict:
            print("Your dictionary is empty!")
        else:
            print("\n📖 Your Saved Words:")
            for g, a in words_dict.items():
                print(f"🇩🇪 {g} : {a}")

    elif action == 'search':
        target = input("Enter the word you are looking for: ")
        if target in words_dict:
            print(f"✅ Found: {target} means {words_dict[target]}")
        else:
            print("❌ Word not found in your dictionary.")

    elif action == 'test':
        if words_dict:
            q = random.choice(list(words_dict.keys()))
            ans = input(f"What is the meaning of '{q}'? ")
            if ans == words_dict[q]:
                print(f"\n⭐ PERFECT {name.upper()}! Correct answer 🏆")
            else:
                print(f"\n❌ Incorrect! The correct meaning is: {words_dict[q]}")
        else:
            print("Add some words first before taking a test!")

    else:
        print("Invalid option, please try again.")
