# -*- coding: utf8 -*-
import os
import datetime
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.api import  memcache

class NewsDB(db.Model):
    user = db.UserProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    title = db.StringProperty()
    text = db.TextProperty()
    
class Main(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        template_values = {'user':user}           
        path = os.path.join(os.path.dirname(__file__), 'admin.html')
        self.response.out.write(template.render(path, template_values))
    def post(self):
        paper = NewsDB()
        if users.get_current_user():
            paper.user = users.get_current_user()
        else:
            paper.user = users.get_current_user()
        #paper.date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        paper.title = self.request.get('title')
        paper.text = self.request.get('content')
        paper.put()
        self.redirect(self.request.uri)
         
"""
class NewsCreator(webapp.RequestHandler):
    def post(self):
        paper = NewsDB()
        if users.get_current_user():
            paper.user = users.get_current_user()
        else:
            paper.user = users.get_current_user()
        #paper.date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        paper.title = self.request.get('title')
        paper.text = self.request.get('content')
        paper.put()
        self.redirect('/admin')
"""
class Coment():            
    def post(self):
        pass   
class News():
    def get(self):
        pass
       
application = webapp.WSGIApplication([('/ivan',Main),
                                      ('/create', NewsCreator),                                                                                                       
                                      ],
                                       debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()