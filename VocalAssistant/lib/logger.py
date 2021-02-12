from time import gmtime, strftime

class Logger:
  __logger = True
  __database_enable = False
  __database = None
  # Constructor
  def __init__ (self, logger = True, database = None):
    self.__logger = logger
    if database:
      self.__database = database
      self.__database_enable = True

  # Current time
  def __current_time (self):
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())
  
  # Default print log
  def print_log (self, string, color):
    # Print only if logger is enabled
    if self.__logger:
      print(f'{ color } [{self.__current_time()}] { string } \033[39m')

  # Default log printer
  def log(self, string):
    self.print_log(string, '\033[32m')
    if self.__database_enable:
      print('Saving LOG in database')
  
  # Info log printer
  def info(self, string):
    self.print_log(string, '\033[34m')
    if self.__database_enable:
      print('Saving INFO in database')

  # Warning log printer
  def warning(self, string):
    self.print_log(string, '\033[33m')
    if self.__database_enable:
      print('Saving WARNING in database')

  # Danger log printer
  def danger(self, string):
    self.print_log(string, '\033[31m')
    if self.__database_enable:
      print('Saving DANGER in database')