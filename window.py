import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
import os, fnmatch


class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        
        files = self.walk_text_directory()

        menu_widget = QListWidget()
        for i in range(len(files)):
            item = QListWidgetItem(f"Text {files[i]}")
            item.setTextAlignment(Qt.AlignLeft)
            menu_widget.addItem(item)

        text_widget = QLabel("Text")
        delete_btn = QPushButton("Delete")
        update_btn = QPushButton("Save/Update")
        generate_btn = QPushButton("Generate Text")
        
        delete_btn.setStyleSheet("background-color: red; color: white;")
        update_btn.setStyleSheet("background-color: blue; color: white;")
        generate_btn.setStyleSheet("background-color: green; color: white;")
        
    

        content_layout = QVBoxLayout()
        content_layout.addWidget(text_widget)
        content_layout.addWidget(delete_btn)
        content_layout.addWidget(update_btn)
        content_layout.addWidget(generate_btn)
        main_widget = QWidget()
        main_widget.setLayout(content_layout)

        layout = QHBoxLayout()
        layout.addWidget(menu_widget, 2)
        layout.addWidget(main_widget, 4)
        self.setWindowTitle("Tinten | Toner | Bildtrommel - Texte Generator")
        self.resize(1024, 768)
        self.setLayout(layout)
        
    # use json
    def walk_text_directory(self):
        files = []
        for root, dirnames, filenames in os.walk('texts'):
            for filename in fnmatch.filter(filenames, '*.txt'):
                files.append(os.path.join(root, filename))
        return files

if __name__ == "__main__":
    app = QApplication()

    w = Widget()
    w.show()

    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())
