import os
import webapp2

from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

from openhci2011.Constants import debugMode

class NotFoundPage(webapp2.RequestHandler):
    def get(self):
        self.response.set_status(404)
        pagePath = os.path.join(os.path.dirname(__file__), "html/404.html")
        pageTemplate = { "path": self.request.path }
        self.response.out.write(template.render(pagePath, pageTemplate))

app= webapp2.WSGIApplication([("/.*", NotFoundPage)], debug=debugMode)
