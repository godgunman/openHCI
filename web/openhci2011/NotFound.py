import os

from google.appengine.dist import use_library
use_library("django", "1.2")
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

from openhci2011.Constants import debugMode

class NotFoundPage(webapp.RequestHandler):
    def get(self):
        self.response.set_status(404)
        pagePath = os.path.join(os.path.dirname(__file__), "html/404.html")
        pageTemplate = { "path": self.request.path }
        self.response.out.write(template.render(pagePath, pageTemplate))

application = webapp.WSGIApplication([("/.*", NotFoundPage)], debug=debugMode)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()

