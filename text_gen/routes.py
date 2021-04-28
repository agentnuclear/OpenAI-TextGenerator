from flask import Blueprint, render_template, request, redirect
# from .generator import ai

generator = Blueprint('generator', __name__)

@generator.route('/')
def index():
    return render_template('Index.html')

@generator.route('/analyze', methods=['POST'])
def analyze():
    title = request.form('title')
    text = ai.generated_text(title)

    return render_template('index.html',text=text)