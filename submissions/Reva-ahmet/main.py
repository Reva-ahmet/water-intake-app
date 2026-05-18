import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QMessageBox

class ThoughtPad(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Reva's Thought Pad")
        self.resize(400, 300)

        layout = QVBoxLayout()

        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Type your thoughts or to-do list here...")
        layout.addWidget(self.text_edit)

        save_button = QPushButton("Save Note")
        save_button.clicked.connect(self.save_note)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def save_note(self):
        note_content = self.text_edit.toPlainText()
        with open("saved_note.txt", "w", encoding="utf-8") as file:
            file.write(note_content)
        QMessageBox.information(self, "Success", "Your note has been saved successfully!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ThoughtPad()
    window.show()
    sys.exit(app.exec())