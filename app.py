from flask import Flask, request, jsonify, render_template
from LLMEnhancer import transform_text
from coverter import PseudoIntellectualEnhancer

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/modify_text',methods=['POST'])
def modify_text():
    data = request.get_json()
    text = data['text']
    mode = data['mode']
    # extracted_text = data.get('text')

    enhancer = PseudoIntellectualEnhancer()
    # modified_text = enhancer.enhance_to_gibberish(extracted_text, complexity_factor=1)
    if mode == 4:
        modified_text = enhancer.enhance_to_gibberish(text, complexity_factor=1)
    else:
        modified_text = transform_text(text, complexity_level=mode)
        

    return jsonify({'text': modified_text})

if __name__ == '__main__':
    app.run(debug=True)
