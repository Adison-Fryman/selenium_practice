#base class for all of our pages, need to pass it a driver
class BasePage(object):
  def __init__(self,driver):
    self.driver = driver
  
 #inside page file going to define a class for every webpage we are going to test.

class MainPage(BasePage):
    def is_title_matches(self):
      return "Python" in self.driver.title
