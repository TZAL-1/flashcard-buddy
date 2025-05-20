import random
from deck import Deck

def main():
    flashcards = Deck()
    while True:
        print("\n~~~ Flashcard Buddy ~~~")
        print("1. Show all cards")
        print("2. Add a new card")
        print("3. Delete a card")
        print("4. Review cards")
        print("5. Quit")
        choice = input("Choose 1-5: ").strip()

        if choice == '1':
            flashcards.list_cards()

        elif choice == '2':
            question = input("Enter the prompt: ")
            answer = input("Enter the answer: ")
            flashcards.add_card(question, answer)
            print("Great! Card added.")

        elif choice == '3':
            flashcards.list_cards()
            try:
                num = int(input(" Which one to delete? ")) - 1
                flashcards.remove_card(num)
                print("Deleted!")
            except:
                print("Hmm, that doesn't look right.")

        elif choice == '4':
            start_review(flashcards)

        elif choice == '5':
            print("Alright, bye!")
            break

        else:
            print("Please pick a number 1–5.")

def start_review(deck):
    if not deck.cards:
        print("Oops, no cards yet. Add some first.")
        return

    to_review = deck.cards[:]
    random.shuffle(to_review)
    total = len(to_review)
    got = 0

    print("Let's go! You have", total, "cards to review.")

    for card in to_review:
        input("Word: " + card.prompt + "  (press Enter for answer)")
        print("Answer:", card.answer)
        resp = input("Did you know it? (y/n) ").strip().lower()
        if resp == 'y':
            got += 1

    print("Done! You got", got, "out of", total, "right.")

if __name__ == '__main__':
    main()
