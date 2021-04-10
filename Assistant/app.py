# from lib.assistant import Assistant

# # Read settings from configuration file
# VA_settings = Assistant.readConfig()
# VA_triggerWord = VA_settings[0]
# VA_name = VA_settings[1]
# VA_gender = VA_settings[2]
# # Read server from ENV variable
# VA_server = os.getenv('SERVER', '')

# vocalAssistant = Assistant(VA_triggerWord, VA_name, VA_gender, VA_server)
# vocalAssistant.run()

# Flask socketio
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from lib.socket_io.assistant import AssistantNamespace

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socket_io = SocketIO(app, cors_allowed_origins="*") # Enable CORS

# Assistant namespace
socket_io.on_namespace(AssistantNamespace('/assistant'))

@app.route('/')
def index():
  return 'Test'

if __name__ == '__main__':
  socket_io.run(app, host='0.0.0.0')
