import os
import datetime

from google.appengine.dist import use_library
use_library("django", "1.2")
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

from openhci2011.Constants import debugMode

class IntroPage(webapp.RequestHandler):
    def get(self):
        pagePath = os.path.join(os.path.dirname(__file__), "html/introAndGoals.html")
        self.response.out.write(template.render(pagePath, None))
    
application = webapp.WSGIApplication([('/2011/intro/', IntroPage), 
                                      ('/2011/goals/', IntroPage), 
                                      ('/2011/introAndGoals/', IntroPage)], debug=debugMode)

def main():
    run_wsgi_app(application)
    
if __name__ == "__main__":
    main()

