class TextEditor:
    def __init__(self):
        self.text = ""
        self.history = []

    def write(self, new_text):
        self.history.append(self.text)
        self.text += new_text

    def undo(self):
        if self.history:
            self.text = self.history.pop()
        return self.text


editor = TextEditor()
editor.write("Hello")
editor.write(" world")
print(editor.undo())  # Hello