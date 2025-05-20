class Card:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

    def to_dict(self):
        return {"prompt": self.prompt, "answer": self.answer}

    @staticmethod
    def from_dict(data):
        return Card(data["prompt"], data["answer"])
