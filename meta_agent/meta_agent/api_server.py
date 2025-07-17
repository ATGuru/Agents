from flask import Flask, request, jsonify
from meta_agent.agent_manager import AgentManager
from meta_agent.user_manager import UserManager
import os

app = Flask(__name__)
agents_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
agent_manager = AgentManager(agents_root)
user_manager = UserManager()

@app.route('/agents', methods=['GET'])
def list_agents():
    return jsonify(agent_manager.list_agents())

@app.route('/agents/<agent_name>/start', methods=['POST'])
def start_agent(agent_name):
    if not user_manager.is_admin():
        return jsonify({'error': 'Unauthorized'}), 403
    agent_manager.start_agent(agent_name)
    return jsonify({'status': 'started'})

@app.route('/agents/<agent_name>/stop', methods=['POST'])
def stop_agent(agent_name):
    if not user_manager.is_admin():
        return jsonify({'error': 'Unauthorized'}), 403
    agent_manager.stop_agent(agent_name)
    return jsonify({'status': 'stopped'})

@app.route('/agents/<agent_name>/status', methods=['GET'])
def agent_status(agent_name):
    return jsonify(agent_manager.agent_info(agent_name))

@app.route('/agents/<agent_name>/log', methods=['GET'])
def agent_log(agent_name):
    return jsonify({'log': agent_manager.agent_log(agent_name)})

if __name__ == '__main__':
    app.run(port=5001)
