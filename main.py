import unittest
from selenium import webdriver
import page

# gives access to methods, run all tests
class PythonOrgSearch(unittest.TestCase):
  
  def setUp(self):
    #put varibles in here
    self.driver = PATH #need to get my path here
    self.driver.get(https://www.python.org/)
  
  def test_example():
    #auto run when running unittest because starts with test
    assert true
    
  def not_a_test():
    pass
  
  def tearDown(self):
    self.driver.close()
    
    
 if __name__ = "__main__": 
  unittest.main()
  
