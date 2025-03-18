from flask import Flask, render_template, request, jsonify
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recognize', methods=['POST'])
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        return jsonify({'text': text})
    except sr.UnknownValueError:
        return jsonify({'text': "Could not understand audio"})
    except sr.RequestError:
        return jsonify({'text': "Error with the speech recognition service"})

if __name__ == '__main__':
    app.run(debug=True)
