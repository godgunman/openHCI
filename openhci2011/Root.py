import os
import logging

from random import randint

from google.appengine.dist import use_library
use_library("django", "1.2")
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app


class MainPage(webapp.RequestHandler):
    def get(self):
        
        logging.info(os.getcwd())

        if self.request.get("m")!="false":
            userAgent = self.request.headers["User-Agent"]
            if "iPad" in userAgent or "iPhone" in userAgent or "iPod" in userAgent or "Android" in userAgent:
                self.redirect("/m/")
                return
        
        pageDict = {"randomNumber": randint(0,6)}
        pagePath = os.path.join(os.path.dirname(__file__), "html/index.html")
        renderResult = template.render(pagePath, pageDict)
        self.response.out.write(renderResult)

application = webapp.WSGIApplication([("/2011", MainPage)])

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
