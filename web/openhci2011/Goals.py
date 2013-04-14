import os
import webapp2

from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

from Constants import debugMode

class MainPage(webapp2.RequestHandler):
    def get(self):
        pagePath = os.path.join(os.path.dirname(__file__), "html/goals.html")
        renderResult = template.render(pagePath, None)
        self.response.out.write(renderResult)

app= webapp2.WSGIApplication([("/goals/", MainPage)], debug=debugMode)
