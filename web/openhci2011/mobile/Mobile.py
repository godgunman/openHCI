import os

from google.appengine.dist import use_library
use_library("django", "1.2")

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

from Constants import debugMode
from Program import addressInfo

class MobilePage(webapp.RequestHandler):
    def get(self):
        pageDict = {"address": addressInfo}
        pagePath = os.path.join(os.path.dirname(__file__), "html/index.html")
        self.response.out.write(template.render(pagePath, pageDict))

application = webapp.WSGIApplication([("/m/", MobilePage)], debug=debugMode)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
