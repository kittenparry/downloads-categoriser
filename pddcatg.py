import sys
import pddcat as pdd

from PySide2.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QGroupBox, QPushButton,\
	QPlainTextEdit, QGroupBox, QCheckBox, QLineEdit, QBoxLayout, QFileDialog

# GUI extension of pddcat using PySide2
# run the following command before launching pddcatg
# pip install -r requirements.txt

class Window(QWidget):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('pddcatg: Porn Download Directory Categoriser GUI')
		self.setGeometry(200, 200, 350, 500)

		self.create_layout()
		self.show()

	def create_layout(self):
		main_box = QVBoxLayout()

		self.console = QPlainTextEdit()
		self.console.setReadOnly(True)
		self.console.setLineWrapMode(self.console.WidgetWidth)
		self.console.setPlainText('testing some text here')

		self.group = QGroupBox('Settings')

		group_vbox = QVBoxLayout()

		src_box = QHBoxLayout()
		self.src_label = QLabel('Source:')
		self.src_input = QLineEdit('')
		self.src_input.setPlaceholderText('src')
		self.src_btn = QPushButton('...')
		src_box.addWidget(self.src_label)
		src_box.addWidget(self.src_input)
		src_box.addWidget(self.src_btn)

		dst_box = QHBoxLayout()
		self.dst_label = QLabel('Destination:')
		self.dst_input = QLineEdit('')
		self.dst_input.setPlaceholderText('dst')
		self.dst_btn = QPushButton('...')
		dst_box.addWidget(self.dst_label)
		dst_box.addWidget(self.dst_input)
		dst_box.addWidget(self.dst_btn)

		names_box = QHBoxLayout()
		self.names_input = QLineEdit()
		self.names_input.setPlaceholderText('Names of models to add to custom list...')
		self.names_add_btn = QPushButton('Add')
		names_box.addWidget(self.names_input)
		names_box.addWidget(self.names_add_btn)

		supporting_box = QHBoxLayout()
		self.sym_check = QCheckBox('Symlinks')
		self.curated_list_btn = QPushButton('Download Curated List of Names')
		supporting_box.addWidget(self.sym_check)
		supporting_box.addWidget(self.curated_list_btn)

		final_box = QHBoxLayout()
		self.help_btn = QPushButton('Help')
		self.run_btn = QPushButton('Run')
		final_box.addWidget(self.help_btn)
		final_box.addWidget(self.run_btn)

		group_vbox.addLayout(src_box)
		group_vbox.addLayout(dst_box)
		group_vbox.addLayout(names_box)
		group_vbox.addLayout(supporting_box)
		group_vbox.addLayout(final_box)
		self.group.setLayout(group_vbox)

		main_box.addWidget(self.console)
		main_box.addWidget(self.group)
		self.setLayout(main_box)

		self.src_btn.clicked.connect(self.get_path)

	def get_path(self):
		print(QFileDialog.getExistingDirectory(self, 'Select Directory'))

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	app.exec_()
	sys.exit()
