# SocketIo stuffs
from flask_socketio import Namespace, emit

# Uptime, CPU and RAM usage lib
import psutil
import os

class AssistantNamespace(Namespace):
  def on_connect(self):
    # Broadcasting the assistant's data, this way all interfaces are updated
    emit('assistant_config_res', assistant_info(self.assistant), broadcast=True)
    emit('device_usage_res', assistant_usage())

  def set_assistant(self, assistant):
    self.assistant = assistant

  def on_assistant_config_get(self, data):
    emit('assistant_config_res', assistant_info(), broadcast=True)

  def on_device_usage_get(self, data):
    emit('device_usage_res', assistant_usage())

def assistant_info(assistant):
  # Server, UUID, Saved, User bind
  response = ['http://127.0.0.1', '', False, False]
  if assistant:
    response = assistant.is_saved()
  # Return the data
  return response

def assistant_usage():
  response = []
  # Get CPU usage
  response.append(psutil.cpu_percent())
  # Get RAM usage
  response.append(psutil.virtual_memory()[2])
  # Return the data
  return response