import os
import zipfile
import requests
import stat
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Translator:

  driver = None

  def __init__(self):
    driver_path = os.path.join(os.getcwd(), 'chromedriver')

    if os.path.isfile(driver_path):
      self.create_driver(driver_path)
    else:
      print('Chrome driver is not found. Downloading...')

      self.download_driver(driver_path)
  
  def download_driver(self, driver_path):
    url = 'https://chromedriver.storage.googleapis.com/113.0.5672.63/chromedriver_mac_arm64.zip'
    zip_file_path = driver_path + '.zip'

    with open(zip_file_path, 'wb') as file:
      response = requests.get(url)
      file.write(response.content)
    
    zip_file = zipfile.ZipFile(zip_file_path)

    zip_file.extract('chromedriver', os.getcwd())
    os.remove(zip_file_path)
    os.chmod(driver_path, stat.S_IEXEC)

    print('Chrome driver is downloaded on {}'.format(driver_path))
    
    self.create_driver(driver_path)

  
  def create_driver(self, driver_path):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    self.driver = webdriver.Chrome(driver_path)
