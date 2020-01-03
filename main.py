from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__, static_folder='static')

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/result', methods = ['POST'])
def answ():
	age = int(request.form['age'])
	sex = int(request.form['sex'])
	cp = int(request.form['cp'])
	trestbps = int(request.form['trestbps'])
	chol = int(request.form['chol'])
	fbs = int(request.form['fbs'])
	restecg = int(request.form['restecg'])
	thalach = int(request.form['thalach'])
	exang = int(request.form['exang'])
	slope = int(request.form['slope'])
	ca = int(request.form['ca'])
	X = np.array((age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, slope, ca)).reshape(1,11)
	model = pickle.load(open('model.sav', 'rb'))
	predict = model.predict(X)[0]
	if predict == 1:
		label = 'You have heart problems'
	else: 
		label = 'You have no heart problems'
	return render_template('result.html', predict = label)
		


if __name__ == '__main__':
	app.run(debug = True)	