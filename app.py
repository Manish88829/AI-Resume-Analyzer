from flask import Flask, render_template, request
import os
from services.parser import extract_text
from services.analyzer import analyze_resume
from services.ats_score import calculate_ats_score

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['resume']
    
    if file:
        path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(path)

        text = extract_text(path)
        analysis = analyze_resume(text)
        score = calculate_ats_score(analysis)

        return render_template('result.html', analysis=analysis, score=score)

if __name__ == '__main__':
    app.run(debug=True)