import json, os
from card import Card

class Deck:
    def __init__(self, filename="flashcards.json"):
        self.filename = filename
        self.cards = []
        self.load()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.cards = [Card.from_dict(d) for d in data]
        else:
            self.cards = []

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([c.to_dict() for c in self.cards], f, indent=2)

    def add_card(self, prompt, answer):
        self.cards.append(Card(prompt, answer))
        self.save()

    def remove_card(self, index):
        if 0 <= index < len(self.cards):
            del self.cards[index]
            self.save()

    def list_cards(self):
        if not self.cards:
            print("No cards yet.")
            return
        for i, c in enumerate(self.cards, 1):
            print(i, ".", c.prompt, "→", c.answer)
