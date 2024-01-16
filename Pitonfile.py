from flask import Flask, render_template, request

app = Flask(__name__)

# Főoldal, ahol a felhasználók bevihetik az adatokat
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Adatok lekérése a felhasználótól
        age = int(request.form['age'])
        gender = request.form['gender']
        stroke = int(request.form['stroke'])
        heart_disease = int(request.form['heart_disease'])
        hypertension = int(request.form['hypertension'])
        diabetes = int(request.form['diabetes'])
        vascular_disease = int(request.form['vascular_disease'])

        # Chads-Vasc pontszám számolása
        chads_vasc_score = calculate_chads_vasc(age, gender, stroke, heart_disease, hypertension, diabetes, vascular_disease)

        return render_template('result.html', chads_vasc_score=chads_vasc_score)

    return render_template('index.html')

# Chads-Vasc pontszám számoló függvény
def calculate_chads_vasc(age, gender, stroke, heart_disease, hypertension, diabetes, vascular_disease):
    chads_vasc_points = 0
    if stroke == 1:
        chads_vasc_points += 1
    if age >= 65:
        chads_vasc_points += 1
    if gender == 'female':
        chads_vasc_points += 1
    if heart_disease == 1:
        chads_vasc_points += 1
    if hypertension == 1:
        chads_vasc_points += 1
    if diabetes == 1:
        chads_vasc_points += 1
    if vascular_disease == 1:
        chads_vasc_points += 1

    return chads_vasc_points

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)#ez egy python file 
