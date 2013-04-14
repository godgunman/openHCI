import os
import webapp2

from google.appengine.dist import use_library
use_library("django", "1.2")

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

from openhci2011.Constants import debugMode
from openhci2011.Program import addressInfo

class MobilePage(webapp2.RequestHandler):
    def get(self):
        pageDict = {"address": addressInfo}
        pagePath = os.path.join(os.path.dirname(__file__), "html/index.html")
        self.response.out.write(template.render(pagePath, pageDict))

app= webapp2.WSGIApplication([("/2011/m/", MobilePage)], debug=debugMode)
