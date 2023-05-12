import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QTextEdit, QPushButton, QTableWidget, QTableWidgetItem, QLabel, QSpacerItem, QSizePolicy


class MyApplication(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.init_table()
        self.init_cpv_keywords_layout()
        self.init_buttons()
        self.init_layout()
        self.table.resizeColumnsToContents()

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

    def init_cpv_keywords_layout(self):
        self.hbox_layout = QHBoxLayout()
        self.hbox_layout.setContentsMargins(0, 0, 0, 0)

        text_edit_cpv = QTextEdit()
        text_edit_cpv.setPlaceholderText("CPV")
        text_edit_keywords = QTextEdit()
        text_edit_keywords.setPlaceholderText("keywords")
        self.hbox_layout.addWidget(text_edit_cpv)
        self.hbox_layout.addWidget(text_edit_keywords)
        self.hbox_widget = QWidget()
        self.hbox_widget.setFixedWidth(800)
        self.hbox_widget.setFixedHeight(50)
        self.hbox_widget.setLayout(self.hbox_layout)

    def init_buttons(self):
        self.button1 = QPushButton("Search")
        self.button1.clicked.connect(self.connect_search_button)
        self.label = QLabel("LOGS")
        self.button2 = QPushButton("Update")
        self.button2.clicked.connect(self.connect_update_button)

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
        link = self.table.item(row, col).text()
        webbrowser.open(link)

    def connect_update_button(self):
        self.label.setText("LOGS UPDATED")

    def connect_search_button(self):
        cpv_text = self.hbox_layout.itemAt(0).widget().toPlainText()
        cpv_number = self.get_correct_cpv_number(cpv_text)
        if cpv_number is False:
            self.label.setText(f"CPV: {cpv_text} is not a number or is more than 8 digits long")
            return
        keywords_text = self.hbox_layout.itemAt(1).widget().toPlainText()
        keywords_list = self.validate_keywords(keywords_text)
        if keywords_list is False: 
            self.label.setText(f"Some keywords contain space or tab characters")
            return
        self.label.setText(f"CPV: {cpv_number}; keywords: {keywords_list}")
    
    def validate_keywords(self, keywords_text):
        keywords_list = keywords_text.split(',')
        keywords_list = list(set(keywords_list))
        for keyword in keywords_list:
            # check if keyword contains whitespace characters
            if keyword.strip() != keyword:
                return False
        return keywords_list

    def get_correct_cpv_number(self, number):
        if self.is_cpv_number_empty(number):
            return None
        if not self.is_cpv_number_valid(number):
            return False
        return number

    def is_cpv_number_empty(self, string):
        string = string.strip('\t\n ')
        if string == "":
            return True
        return False

    def is_cpv_number_valid(self, string):
        if string.isdigit() and len(string) <= 8:
            return True
        return False

    def closeEvent(self, event):
        self.cleanup_resources()
        self.close_csv()
        event.accept()
        
    def close_csv(self):
        pass
    
    def cleanup_resources(self):
        self.table.clearContents()
        self.table.setRowCount(0)
        self.table.setColumnCount(0)
        self.hbox_layout.itemAt(0).widget().clear()
        self.hbox_layout.itemAt(1).widget().clear()
        self.button1.clicked.disconnect()
        self.button2.clicked.disconnect()
        self.label.clear()

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApplication()
    window.resize(1200, 800)
    sys.exit(app.exec_())
