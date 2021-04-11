# Vocal assistant class
from lib.assistant import Assistant
# Flask socketIo
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
# Flask csrf module
from flask_wtf.csrf import CSRFProtect
# Vocal Assistant socket's namespace
from lib.socket_io.assistant import AssistantNamespace
# OS for env variable and other pourpose
import os

# --- Vocal assistant configuration ---
# Read settings from configuration file
VA_settings = Assistant.read_config()
VA_triggerWord = VA_settings[0]
VA_name = VA_settings[1]
VA_gender = VA_settings[2]
# Read server from ENV variable
VA_server = os.getenv('SERVER', '')

vocalAssistant = Assistant(VA_triggerWord, VA_name, VA_gender, VA_server)

# --- Flask configuration ---
app = Flask(__name__)
# CSRF Protection (suggested by SonarCloud)
csrf = CSRFProtect(app)
# Flask secret key. Get from env variable or generate at the moment
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', os.urandom(16))
# Create socketIo instance
if os.getenv('DEBUG', 'False') == 'True':
  socket_io = SocketIO(app, cors_allowed_origins="*", logger=True, engineio_logger=True) # Dev configuration
else:
  socket_io = SocketIO(app, cors_allowed_origins="*") # Production configuration

# Assistant namespace
socket_io.on_namespace(AssistantNamespace('/assistant'))

@app.route('/')
def index():
  return 'Server is up and running!'

if __name__ == '__main__':
  # Run socketIon
  socket_io.run(app, host='0.0.0.0')
  # Start vocal assistant
  vocalAssistant.run()
