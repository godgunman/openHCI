import os
import datetime

from google.appengine.dist import use_library
use_library("django", "1.2")
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

from Constants import debugMode

class ManifestHandler(webapp.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/cache-manifest"

        fileName = self.request.path.split('/')[2]
        manifestPath = os.path.join(os.path.dirname(__file__), fileName)

        self.response.out.write(template.render(manifestPath, None))
    
app = webapp.WSGIApplication([('/manifest/cache.manifest', ManifestHandler),
                              ('/manifest/mobilecache.manifest', ManifestHandler)], debug=debugMode)

def main():
    run_wsgi_app(app)

if __name__ == "__main__":
    main()
