import random

words_dict = {}
name = input("Enter your name: ")

try:
    with open("dictionary.txt", "r", encoding="utf-8") as file:
        for line in file:
            if ":" in line:
                key, value = line.strip().split(":")
                words_dict[key] = value
    print(f"Perfect ✅ {name}! تم تحميل {len(words_dict)} كلمة من ملفك.")
except:
    print(f"Perfect ✅ {name}! نبدأ قاموس جديد ")

while True:
    print("\n" + "=" * 40)
    action = input("Type (add) لزيادة كلمة, (test) للاختبار, (show) للعرض, (search) للبحث, (exit) للخروج: ").lower()

    if action == 'exit':
        print(f"👋 مع السلامة يا {name.upper()}!.")
        break

    elif action == 'add':
        word = input("Enter German word: ")
        meaning = input("Enter Arabic meaning: ")
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

        print(f" تم الحفظ! مستواك الحالي: {rank}")

    elif action == 'show':
        if not words_dict:
            print(" القاموس لسه فاضي!")
        else:
            print("\n📖 كلماتك المحفوظة:")
            for g, a in words_dict.items():
                print(f"{g} : {a}")

    elif action == 'search':
        target = input(" اكتب الكلمة اللي بتدور عليها: ")
        if target in words_dict:
            print(f"✅ لقيناها: {target} معناها بالعربي {words_dict[target]}")
        else:
            print("❌ الكلمة دي مش موجودة في قاموسك.")

    elif action == 'test':
        if words_dict:
            q = random.choice(list(words_dict.keys()))
            ans = input(f"شو معنى كلمة '{q}'؟ ")
            if ans == words_dict[q]:
                print(f"\n⭐ PERFECT {name.upper()}! إجابة صحيحة 🏆")
            else:
                print(f"\n❌ للاسف غلط! المعنى الصح هو: {words_dict[q]}")
        else:
            print(" لازم تضيف كلمات الأول عشان نختبرك!")

    else:
        print(" اختيار غير صحيح، حاول تاني.")