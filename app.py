from flask import Flask, render_template, request, redirect, url_for
import os
import numpy as np

# Optional (model use करत असशील तर uncomment कर)
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image

app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Model load (optional)
# model = load_model('model/plant_model.h5')

# Dummy classes (तू नंतर change करू शकतेस)
classes = ['Healthy', 'Tomato Leaf Spot', 'Tomato Blight', 'Tomato Mosaic Virus']


# ---------------- ROUTES ---------------- #

@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


from flask import Flask, render_template, request, redirect, url_for

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        farmer_id = request.form['farmer_id']
        password = request.form['password']

        if username == "admin" and farmer_id == "123" and password == "123":
            return redirect(url_for('login'))   # 🔥 refresh page
        else:
            return render_template('login.html', error="Invalid Login")

    return render_template('login.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return "No file uploaded"

    file = request.files['image']
    if file.filename == '':
        return "No selected file"

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # --------- DUMMY PREDICTION ---------
    # Random result for demo
    result = np.random.choice(classes)
    confidence = round(np.random.uniform(80, 99), 2)

    # --------- REAL MODEL (optional) ---------
    """
    img = image.load_img(filepath, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    prediction = model.predict(img_array)
    result = classes[np.argmax(prediction)]
    confidence = round(np.max(prediction) * 100, 2)
    """

    return render_template('result.html',
                           prediction=result,
                           confidence=confidence,
                           img_path=filepath)


# ---------------- RUN ---------------- #

if __name__ == '__main__':
    app.run(debug=True)