import os
import datetime
import webapp2

from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

from openhci2011.Constants import debugMode

class IntroPage(webapp2.RequestHandler):
    def get(self):
        pagePath = os.path.join(os.path.dirname(__file__), "html/introAndGoals.html")
        self.response.out.write(template.render(pagePath, None))
    
app= webapp2.WSGIApplication([('/2011/intro/', IntroPage), 
  ('/2011/goals/', IntroPage), 
  ('/2011/introAndGoals/', IntroPage)], debug=debugMode)
