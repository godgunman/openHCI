import webapp2
import logging

class MainPage(webapp2.RequestHandler):
    def get(self):
      self.redirect("/2009/Home.html")

app = webapp2.WSGIApplication([('/2009.*', MainPage)],
                              debug=True)
