'''Fronend'''

import sys
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem


# app = QApplication([])
# label = QLabel()
# label.setOpenExternalLinks(True)  # open links in a web browser when clicked
# label.setWordWrap(True)  # wrap long text
# label.setTextFormat(Qt.RichText)  # enable HTML formatting
# label.setText("<a href='https://example.com'>Click me!</a>")
# label.show()
# app.exec_()

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel
# from PyQt5.QtCore import Qt, QUrl
# from PyQt5.QtGui import QDesktopServices


# class DataWidget(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()

#     def init_ui(self):
#         # Create the main layout
#         layout = QVBoxLayout()

#         # Create the QTableWidget
#         table = QTableWidget()

#         # Set the number of rows and columns
#         table.setRowCount(3)  # Number of rows
#         # Number of columns (including the link column)
#         table.setColumnCount(5)

#         # Set the column headers
#         table.setHorizontalHeaderLabels(
#             ["Column 1", "Column 2", "Column 3", "Column 4", "Links"])

#         # Populate the table with data
#         for row in range(table.rowCount()):
#             for col in range(table.columnCount() - 1):  # Exclude the link column
#                 item = QTableWidgetItem(f"Row {row + 1}, Col {col + 1}")
#                 table.setItem(row, col, item)

#             link_item = QTableWidgetItem()
#             link_label = QLabel("<a href='https://www.example.com'>Link</a>")
#             link_label.setTextFormat(Qt.RichText)
#             link_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
#             link_label.setOpenExternalLinks(True)
#             link_item.setData(Qt.WidgetShortcut, link_label)
#             table.setItem(row, table.columnCount() - 1, link_item)

#         # Set the cell widget for the link column to display the links
#         table.setCellWidget(0, table.columnCount(
#         ) - 1, QLabel("<a href='https://www.example.com'>Link 1</a>"))
#         table.setCellWidget(1, table.columnCount(
#         ) - 1, QLabel("<a href='https://www.example.com'>Link 2</a>"))
#         table.setCellWidget(2, table.columnCount(
#         ) - 1, QLabel("<a href='https://www.example.com'>Link 3</a>"))

#         # Resize the columns to fit the contents
#         table.resizeColumnsToContents()

#         # Add the table to the layout
#         layout.addWidget(table)

#         # Set the main layout for the widget
#         self.setLayout(layout)

#         self.setWindowTitle("Data Widget")
#         self.show()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     widget = DataWidget()
#     sys.exit(app.exec_())


# from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPushButton, QWidget


# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         x_pos, y_pos = 10, 10
#         w_pix, h_pix = 150, 150

#         container = QWidget(self)
#         container.setContentsMargins(0, 0, 0, 0)
#         container.setFixedSize(w_pix, h_pix)
#         container.move(x_pos, y_pos)
#         container.setStyleSheet("background-color:salmon;")

#         hbox = QHBoxLayout(container)
#         hbox.setContentsMargins(0, 0, 0, 0)

#         self.okButton = QPushButton("OK")
#         self.cancelButton = QPushButton("Cancel")

#         hbox.addWidget(self.okButton)
#         hbox.addWidget(self.cancelButton)

#         self.resize(640, 480)


# if __name__ == "__main__":
#     import sys

#     app = QApplication(sys.argv)
#     ex = Example()
#     ex.show()
#     sys.exit(app.exec_())


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton

app = QApplication(sys.argv)

# Create a QWidget as the main window
window = QWidget()

# Create a QVBoxLayout
main_layout = QVBoxLayout()

# Create the first QHBoxLayout
hbox1_layout = QHBoxLayout()
hbox1_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins

# Create the second QHBoxLayout
hbox2_layout = QHBoxLayout()
hbox2_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins

# Create the first horizontal layout with fixed size
hbox1_widget = QWidget()
hbox1_widget.setFixedWidth(800)
hbox1_widget.setFixedHeight(100)
hbox1_widget.setLayout(hbox1_layout)

# Create the second horizontal layout with fixed size
hbox2_widget = QWidget()
hbox2_widget.setFixedWidth(800)
hbox2_widget.setFixedHeight(500)
hbox2_widget.setLayout(hbox2_layout)

# Create the button
button = QPushButton("Button")

# Create QTextEdit widgets
text_edit1 = QTextEdit()
text_edit2 = QTextEdit()

# Add QTextEdit widgets to the first QHBoxLayout
hbox1_layout.addWidget(text_edit1)

# Add QTextEdit widgets to the second QHBoxLayout
hbox2_layout.addWidget(text_edit2)

# Add the first horizontal layout to the main QVBoxLayout
main_layout.addWidget(hbox1_widget)

# Add the second horizontal layout to the main QVBoxLayout
main_layout.addWidget(hbox2_widget)

# Add the button to the main QVBoxLayout
main_layout.addWidget(button)

# Set the layout for the main window
window.setLayout(main_layout)

# Show the main window
window.show()

sys.exit(app.exec_())
