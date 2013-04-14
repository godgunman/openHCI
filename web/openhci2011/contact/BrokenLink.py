import webapp2

from Constants import debugMode

from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import mail

class BrokenLinkHandler(webapp2.RequestHandler):
    def post(self):
        path = self.request.get("path")
        msg = self.request.get("message")
        mailBody = "path: " + path + "\nmsg:  " + msg
        mail.send_mail(sender="webmaster@openhci.com",
                   reply_to="webmaster@openhci.com",
                   to="webmaster@openhci.com",
                   subject="Broken Link",
                   body=mailBody)
        self.redirect("/")
    
app = webapp2.WSGIApplication([('/brokenLink/', BrokenLinkHandler)], debug=debugMode)
