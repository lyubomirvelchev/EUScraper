"""Original frontend"""

import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QTextEdit, QPushButton, QTableWidget, QTableWidgetItem, QLabel, QSpacerItem, QSizePolicy


class MyApplication(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.init_table()
        self.init_cpv_description_layout()
        self.init_buttons()
        self.init_layout()

    def init_table(self):
        self.table = QTableWidget()
        self.table.setRowCount(40)
        self.table.setColumnCount(3)

        self.table.setHorizontalHeaderLabels(["Column 1", "HUI", "links"])
        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount() - 1):  # Exclude the link column
                item = QTableWidgetItem(f"Row {row + 1}, Col {col + 1}")
                self.table.setItem(row, col, item)

            if row % 2:
                link_item = QTableWidgetItem("https://www.example.com")
                self.table.setItem(
                    row, self.table.columnCount() - 1, link_item)
            else:
                link_item = QTableWidgetItem(
                    "https://etendering.ted.europa.eu/cft/cft-display.html?cftId=14303")
                self.table.setItem(
                    row, self.table.columnCount() - 1, link_item)

        self.table.cellDoubleClicked.connect(self.open_link)
        self.table.resizeColumnsToContents()

    def init_cpv_description_layout(self):
        self.hbox_layout = QHBoxLayout()
        self.hbox_layout.setContentsMargins(0, 0, 0, 0)

        text_edit_cpv = QTextEdit()
        text_edit_cpv.setPlaceholderText("CPV")
        text_edit_description = QTextEdit()
        text_edit_description.setPlaceholderText("Description")
        self.hbox_layout.addWidget(text_edit_cpv)
        self.hbox_layout.addWidget(text_edit_description)
        self.hbox_widget = QWidget()
        self.hbox_widget.setFixedWidth(800)
        self.hbox_widget.setFixedHeight(50)
        self.hbox_widget.setLayout(self.hbox_layout)

    def init_buttons(self):
        self.button1 = QPushButton("Search")
        self.label = QLabel("LOGS")
        self.button2 = QPushButton("Update")

    def init_layout(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.table)
        main_layout.addWidget(self.hbox_widget)
        main_layout.addWidget(self.button1)
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.button2)

        self.setLayout(main_layout)

        self.setWindowTitle("My Application")
        self.show()

    def open_link(self, row, col):
        print(row, col)
        link = self.table.item(row, col).text()
        print(link)
        webbrowser.open(link)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApplication()
    window.resize(800, 600)
    sys.exit(app.exec_())
