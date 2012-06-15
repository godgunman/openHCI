from Constants import debugMode

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import mail

class BrokenLinkHandler(webapp.RequestHandler):
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
    
app = webapp.WSGIApplication([('/brokenLink/', BrokenLinkHandler)], debug=debugMode)
    
def main():
    run_wsgi_app(app)
    
if __name__ == "__main__":
    main()
    
