# from lib.assistant import Assistant
import asyncio
import os
import socketio
import socket
from sanic import Sanic
import psutil
import time

# # Read settings from configuration file
# VA_settings = Assistant.readConfig()
# VA_triggerWord = VA_settings[0]
# VA_name = VA_settings[1]
# VA_gender = VA_settings[2]
# # Read server from ENV variable
# VA_server = os.getenv('SERVER', '')

# vocalAssistant = Assistant(VA_triggerWord, VA_name, VA_gender, VA_server)
# vocalAssistant.run()

# Socket for transmit the data to the basic interface

sio = socketio.AsyncServer(async_mode='sanic', cors_allowed_origins="*")
app = Sanic(name='AssistantServer')
sio.attach(app)

print('Socket is on!')

@sio.on('assistant.info.get', namespace='/interface')
def getAssistantInfo (sid):
  response = [] 
  # Check if it's connected to internet
  response.append(isConnected())
  # TODO Need to manage this!!!
  # Check if socket of the assistant is connected
  response.append(True)
  # Return data
  return response

@sio.on('device.usage.get', namespace='/interface')
def getDeviceInfo (sid):
  response = []
  # Get CPU usage
  load1, load5, load15 = psutil.getloadavg()
  response.append((load15/os.cpu_count()) * 100)
  # Get RAM usage
  response.append(psutil.virtual_memory()[2])
  # Get device time
  # From StackOverflow https://stackoverflow.com/questions/2598145/how-to-retrieve-the-process-start-time-or-uptime-in-python#answer-4559733
  response.append(time.CLOCK_UPTIME)
  print(response[2])
  # Return data
  return response


# From StackOverflow https://stackoverflow.com/questions/20913411/test-if-an-internet-connection-is-present-in-python#answer-62115290
# TODO Is google.com available in all states?
def isConnected():
  try:
      # Try to socket to google.com
      sock = socket.create_connection(("www.google.com", 80))
      if sock is not None:
        sock.close
      return True
  except OSError:
      pass
  return False

if __name__ == '__main__':
  app.run()