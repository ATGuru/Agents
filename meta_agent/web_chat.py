from flask import Flask, render_template, request, jsonify
import threading
from meta_agent.main import MetaAgent
import os

app = Flask(__name__)
meta_agent = MetaAgent()

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = meta_agent.handle_prompt(user_input)
    return jsonify({'response': str(response)})

def run_flask():
    app.run(port=5002, debug=True)

if __name__ == '__main__':
    threading.Thread(target=run_flask).start()
