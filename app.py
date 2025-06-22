from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import numpy as np
import pickle

app = Flask(__name__, template_folder='template', static_folder='static')

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Somu@123'
app.config['MYSQL_DB'] = 'predictive_maintenance'

mysql = MySQL(app)

# Load the model once at startup
try:
    with open('a.dat', 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    model = None
    print(f"Error loading model: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Map machine type
        type_map = {'L': 0, 'M': 1, 'H': 2}
        type_input = request.form['Type']
        type_value = type_map.get(type_input, 0)

        # Get form values
        air_temp = float(request.form['Air temperature'])
        process_temp = float(request.form['Process temperature'])
        rot_speed = float(request.form['Rotational speed'])
        torque = float(request.form['Torque'])
        tool_wear = float(request.form['Tool wear'])

        # Prepare input
        input_data = [type_value, air_temp, process_temp, rot_speed, torque, tool_wear]
        input_array = np.array(input_data).reshape(1, -1)

        # Predict
        prediction = model.predict(input_array)[0]
        probability = model.predict_proba(input_array)[0][prediction]
        result_text = '→ No Failure\nMachine was OK.' if prediction == 0 else '→ Failure Occurred\nMachine failed.'

        # Save to MySQL
        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO prediction_history (
                machine_type, air_temperature, process_temperature,
                rotational_speed, torque, tool_wear,
                prediction_result, probability, prediction_text
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            type_input, air_temp, process_temp, rot_speed,
            torque, tool_wear, prediction, probability, result_text
        ))
        mysql.connection.commit()
        cur.close()

        return render_template("predict.html", prediction=prediction, probability=probability, str=result_text)

    except Exception as e:
        return f"Error during prediction: {str(e)}"

@app.route('/history')
def history():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM prediction_history ORDER BY id DESC")
        rows = cur.fetchall()
        cur.close()
        return render_template('history.html', rows=rows)
    except Exception as e:
        return f"Error fetching history: {str(e)}"

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
