from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self, ai_assistant):
        super().__init__()
        self.ai_assistant = ai_assistant
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Type your message...")
        self.input_field.returnPressed.connect(self.process_input)
        layout.addWidget(self.input_field)

        self.send_button = QPushButton("Send", self)
        self.send_button.clicked.connect(self.process_input)
        layout.addWidget(self.send_button)

        self.conversation_view = QTextEdit(self)
        self.conversation_view.setReadOnly(True)
        layout.addWidget(self.conversation_view)

        self.setWindowTitle("Urdu AI Assistant")
        self.setGeometry(100, 100, 600, 400)

    def process_input(self):
        user_input = self.input_field.text()
        self.conversation_view.append(f"<p style='color:#000000'>You: {user_input}</p>")
        self.input_field.clear()

        response = self.ai_assistant.generate_response(user_input)
        self.conversation_view.append(f"<p style='color:#808080'>AI Assistant: {response}</p>")
        self.ai_assistant.speak_response(response)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return and not self.input_field.hasFocus():
            self.process_input()
        super().keyPressEvent(event)
