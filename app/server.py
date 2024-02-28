from flask import Flask,render_template, request
from app.utils.image import save_image,read_image
from app.utils.prediction import get_kannada_prediction
from app.kannada.translation import get_translation

kannada = []
app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static",
    )

def run():
    app.run()

@app.route("/", methods=["POST", "GET"])
def home():   
    if request.method == "POST":
        img64 = request.form['my_hidden']
        image_path = save_image(img64)
        image_data = read_image(image_path)
        predicted_character = get_kannada_prediction(image_data)
        kannada.append(predicted_character)
        print("PREDICTION CHAR = ",predicted_character)
        if len(kannada)%3==0:
            kannada_str = ''.join(kannada)
            english = get_translation(kannada_str)
            result= "Kannada : {}, English: {}".format(''.join(kannada),english)
            kannada.clear()
            return render_template("show_prediction.html",output=result)
        else:
            return render_template("home.html")
   
    return render_template("home.html")


