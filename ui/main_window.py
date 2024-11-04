from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QTextEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QMessageBox
)
from PyQt5.QtCore import Qt
from services.text_generator import TextGenerator

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ассистент отельера")

        self.init_ui()
        self.text_generator = TextGenerator()

    def init_ui(self):
        # Поля ввода
        self.name_input = QLineEdit()
        self.location_input = QLineEdit()
        self.type_input = QLineEdit()
        self.amenities_input = QLineEdit()

        # Выбор тона текста
        self.tone_combo = QComboBox()
        self.tone_combo.addItems(["Дружелюбный", "Официальный", "Маркетинговый"])

        # Кнопка генерации
        self.generate_button = QPushButton("Сгенерировать описание")
        self.generate_button.clicked.connect(self.generate_description)

        # Поле вывода
        self.description_output = QTextEdit()
        self.description_output.setReadOnly(True)

        # Layouts
        layout = QVBoxLayout()

        layout.addLayout(self.create_form_layout("Название отеля*", self.name_input))
        layout.addLayout(self.create_form_layout("Местоположение(город, страна)*", self.location_input))
        layout.addLayout(self.create_form_layout("Тип отеля(например, курортный отель)*", self.type_input))
        layout.addLayout(self.create_form_layout("Удобства", self.amenities_input))
        layout.addLayout(self.create_form_layout("Тон текста", self.tone_combo))

        layout.addWidget(self.generate_button)
        layout.addWidget(QLabel("Сгенерированное описание:"))
        layout.addWidget(self.description_output)

        self.setLayout(layout)

    def create_form_layout(self, label_text, widget):
        layout = QHBoxLayout()
        label = QLabel(label_text)
        label.setFixedWidth(220)
        layout.addWidget(label)
        layout.addWidget(widget)
        return layout

    def generate_description(self):
        # Получаем данные
        name = self.name_input.text()
        location = self.location_input.text()
        hotel_type = self.type_input.text()
        amenities = self.amenities_input.text()
        tone = self.tone_combo.currentText()

        # Проверка обязательных полей
        if not name or not location or not hotel_type:
            QMessageBox.warning(self, "Предупреждение", "Пожалуйста, заполните все обязательные поля.")
            return

        # Генерация описания
        description = self.text_generator.generate(
            name=name,
            location=location,
            hotel_type=hotel_type,
            amenities=amenities,
            tone=tone
        )
        # Установка в поле для описания  
        self.description_output.setText(description)