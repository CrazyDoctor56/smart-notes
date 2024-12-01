from PyQt6.QtWidgets import (QApplication, QMainWindow, QInputDialog)
from ui import Ui_MainWindow
import json

app = QApplication([])
win = QMainWindow()
ui = Ui_MainWindow()

ui.setupUi(win)
#----------------------------------------------------------------

NOTES = {
    "нотатка №1": {
        "текст": "Люди я не діма",
        "теги": ["покупка", "хліб"]
    },

    "нотатка №2": {
        "текст": "на треню",
        "теги": ["Діма", "треня"]
    },
}

with open("notes_data.json", "r", encoding = "UTF-8") as file:
    NOTES = json.load(file)    

ui.notes_list.addItems(NOTES)


def show_note():
    note_name = ui.notes_list.selectedItems()[0].text()
    note = NOTES[note_name]
    ui.textEdit.setText(note["текст"])
    ui.tags_list.clear()
    ui.tags_list.addItems(note["теги"])

ui.notes_list.itemClicked.connect(show_note)

def add_notes():
    note_name, ok = QInputDialog.getText(
        win, "Додати нотатку", "Назва нотатки:"
    )

    if ok:
        NOTES[note_name] = {
            "текст": "",
            "теги": [],
        }
    
        ui.notes_list.addItem(note_name)

ui.btn_create_note.clicked.connect(add_notes)


def save_note():
    if ui.notes_list.selectedItems():
        note_name = ui.notes_list.currentItem().text()
        note_text = ui.textEdit.toPlainText()

        NOTES[note_name] = {
            "текст": note_text,
            "теги": [],
        }

        with open("notes_data.json", "w", encoding = "UTF-8") as file:
            json.dump(NOTES, file)

ui.btn_save_note.clicked.connect(save_note)


    
#----------------------------------------------------------------
win.show()
app.exec()