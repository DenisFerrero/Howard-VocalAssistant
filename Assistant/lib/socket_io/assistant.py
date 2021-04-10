from flask_socketio import Namespace, emit

# Uptime, CPU and RAM usage lib
import psutil
import time
import os

class AssistantNamespace(Namespace):
  def on_connect(self):
    # Broadcasting the assistant's data, this way all interfaces are updated
    emit('assistant_config_res', assistant_info(), broadcast=True)
    emit('device_usage_res', assistant_usage())

  def on_assistant_config_get(self, data):
    emit('assistant_config_res', assistant_info(), broadcast=True)

  def on_device_usage_get(self, data):
    emit('device_usage_res', assistant_usage())

def assistant_info():
  response = []
  # TODO Manage
  # Server address
  response.append('http://127.0.0.1')
  # UUID if the assistant is saved
  response.append('')
  # Check if the assistant is saved
  response.append(False)
  # Check if the assistant is registered to a user
  response.append(False)
  # Return the data
  return response

def assistant_usage():
  response = []
  # Get CPU usage
  load1, load5, load15 = psutil.getloadavg()
  response.append((load15/os.cpu_count()) * 100)
  # Get RAM usage
  response.append(psutil.virtual_memory()[2])
  # Get device time
  # From StackOverflow https://stackoverflow.com/questions/2598145/how-to-retrieve-the-process-start-time-or-uptime-in-python#answer-4559733
  response.append(time.time() - psutil.boot_time())
  # Return the data
  return response