from flask_socketio import Namespace

# Connection utility
from urllib.error import URLError
from urllib.request import urlopen 

# Uptime and CPU, RAM count lib
import psutil
import time
import os

class AssistantNamespace(Namespace):
  def assistant_info_get(self):
    response: []
    # Check if it's connected to internet
    response.append(is_connected())
    # TODO Manage
    # Check if the socket to the target server is connected
    response.append(True)
    return response

  def device_usage_get(self):
    response = []
    # Get CPU usage
    load1, load5, load15 = psutil.getloadavg()
    response.append((load15/os.cpu_count()) * 100)
    # Get RAM usage
    response.append(psutil.virtual_memory()[2])
    # Get device time
    # From StackOverflow https://stackoverflow.com/questions/2598145/how-to-retrieve-the-process-start-time-or-uptime-in-python#answer-4559733
    response.append(time.time() - psutil.boot_time())
    # Return data
    return response

# From StackOverflow https://stackoverflow.com/questions/3764291/checking-network-connection#answer-3764660
# TODO Is google.com available in all states?
def is_connected():
  try:
    # Try connection to google.com
    urlopen('https://google.com', timeout=1)
    return True
    # If the connection fail
  except URLError as err: 
    return False
