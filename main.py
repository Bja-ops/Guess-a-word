import random

names = ["Bartek", "Adam", "Konrad",
         "Kacper", "Sebastian", "Joachim",
              "Paweł", "Albert", "Dawid"
              "Diana", "Aleksandra", "Oliwia",
              "Łucja", "Gabrysia", "Kinga",
              "Katarzyna", "Wiktoria", "Karina"]

fruits = ["jabłko", "banan", "gruszka",
          "arbuz", "truskawka", "malina",
          "jerzyna", "pomarańcz", "śliwka",
          "brzoskwinia", "nektarynka", "jarzębina"]

vegetables = ["brokuł", "seler", "marchew",
              "pasternak", "ziemniak", "pomidor",
              "rzodkiewka", "kapusta", "sałata",
              "cebula", "batat", "papryka"]
target_name = random.choice(names)

category = input("Podaj kategorię (imie, owoce, warzywa, zwierzęta): ")
if category == "imie":
    print("Zgadnij imię! Podpowiedź: imię ma", len(target_name), "liter.")
    while True:
        guess = input("Podaj imię: ")
        if guess == target_name:
            print("Zgadłeś!")
            break
        else:
            print("Nie zgadłeś, spróbuj ponownie.")
elif category == "owoce":
    target_fruit = random.choice(fruits)
    print("Zgadnij owoc! Podpowiedź: owoc ma", len(target_fruit), "liter.")
    while True:
        guessF = input("Podaj owoc: ")
        if guessF == target_fruit:
            print("Zgadłeś!")
            break
        else:
            print("Nie zgadłeś, spróbuj ponownie")
elif category == "warzywa":
    target_vegetable = random.choice(vegetables)
    print("Zgadnij warzywo! Podpowiedź, ma ono", len(target_vegetable), "liter.")
    while True:
        guessV = input("Podaj warzywo: ")
        if guessV == target_vegetable:
            print("Zgadłeś! ")
            break
        else:
            print("Nie zgadłeś, spóbuj ponownie")
