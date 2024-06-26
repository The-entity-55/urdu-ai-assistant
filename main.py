import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow
from src.ai_assistant import AIAssistant

def main():
    app = QApplication(sys.argv)
    ai_assistant = AIAssistant()
    main_window = MainWindow(ai_assistant)
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
