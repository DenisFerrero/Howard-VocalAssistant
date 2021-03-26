from time import gmtime, strftime
import os

class Logger:
  __debug = False

  def __init__ (self):
    self.__debug = os.getenv('DEBUG', 'False') == 'True'

  # Current time
  def __current_time (self):
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())
  
  # Default print log
  def print_log (self, string, color):
    print(f'{ color } [{self.__current_time()}] { string } \033[39m')

  # Default log printer
  def log(self, string):
    self.print_log(string, '\033[32m')
  
  # Info log printer
  def info(self, string):
    self.print_log(string, '\033[34m')

  # Warning log printer
  def warning(self, string):
    self.print_log(string, '\033[33m')

  # Danger log printer
  def danger(self, string):
    self.print_log(string, '\033[31m')

  # Debug log printer
  def debug(self, string):
    if self.__debug:
      self.print_log(string, '\033[35m')