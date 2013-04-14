import os
import logging
import webapp2

from random import randint

from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
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

app= webapp2.WSGIApplication([("/2011", MainPage)])

