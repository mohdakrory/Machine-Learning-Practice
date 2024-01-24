from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QLineEdit, QPushButton
from PyQt5 import uic
import sys
from datetime import datetime
from pickle import load

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# Load the ui file
		uic.loadUi("salary_predictor.ui", self)

		self.gender = self.findChild(QComboBox, "gender")
		self.doj = self.findChild(QLineEdit, "doj")
		self.current_date = self.findChild(QLineEdit, "current_date")
		self.designation = self.findChild(QComboBox, "designation")
		self.age = self.findChild(QLineEdit, "age")
		self.unit = self.findChild(QComboBox, "unit")
		self.leaves_used = self.findChild(QLineEdit, "leaves_used")
		self.rating = self.findChild(QComboBox, "rating")
		self.gender = self.findChild(QComboBox, "gender")
		self.past_exp = self.findChild(QLineEdit, "past_exp")
		self.predict_btn = self.findChild(QPushButton, "predict")
		self.result = self.findChild(QLineEdit, "result")

		# set placeholders for each QLineEdit element 
		self.doj.setPlaceholderText("mm-dd-yyyy")
		self.current_date.setPlaceholderText("mm-dd-yyyy")

		self.predict_btn.clicked.connect(self.predict_salary)

		# Show The App
		self.show()

	def predict_salary(self):

		print(self.gender.currentText())
		print(self.doj.text())
		print(self.current_date.text())
		print(self.designation.currentText())
		print(self.current_date.text())
		print(self.age.text())
		print(self.unit.currentText())
		print(self.leaves_used.text())
		print(self.rating.currentText())
		print(self.past_exp.text())


		sample = [
			 self.gender.currentText(),
			 self.doj.text(),
			 self.current_date.text(),
			 self.designation.currentText(),
			 float(self.age.text()),
			 self.unit.currentText(),
			 float(self.leaves_used.text()),
			 30 - float(self.leaves_used.text()),
			 float(self.rating.currentText()),
			 float(self.past_exp.text())
			 ]
		SEX_mapping = {'Female': 0, 'Male': 1}

		designation_mapping = {
			'Analyst': 0,
			'Senior Analyst': 1,
			'Associate': 2,
			'Manager': 3,
			'Senior Manager': 4,
			'Director': 5
		}

		sample[0] = SEX_mapping[sample[0]]

		sample[3] = designation_mapping[sample[3]]

		date_format = "%m-%d-%Y"
		start_date = datetime.strptime(sample[1], date_format)
		end_date = datetime.strptime(sample[2], date_format)

		months_difference = (end_date - start_date).days // 30

		sample.append(months_difference)

		sample.pop(2)
		sample.pop(1)
		
		for i in ['Finance', 'IT', 'Operations', 'Marketing', 'Web']:
			sample.append(int(sample[3] == i))
			
		sample.pop(3)

		with open('RandomForestRegressor_n=200.pkl', 'rb') as file:
			RandomForestRegressor = load(file)

		res = RandomForestRegressor.predict([sample])[0]
		self.result.setText(f'{int(res)}')

# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()

