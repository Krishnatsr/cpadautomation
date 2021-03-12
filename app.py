from flask import Flask

app = Flask(__name__)

from pyvirtualdisplay import Display
from selenium import webdriver

@app.route("/")
def data():
  with Display():
      # we can now start Firefox and it will run inside the virtual display
      browser = webdriver.Firefox()
      # put the rest of our selenium code in a try/finally
      # to make sure we always clean up at the end
      try:
          browser.get('http://www.google.com')
          print(browser.title) #this should print "Google"
      finally:
          browser.quit()
      return browser.title


if(__name__ == "__main__"):
  app.run()
