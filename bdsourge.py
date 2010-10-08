from google.appengine.ext import db


class NewsDB(db.Model):
    user = db.UserProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    title = db.StringProperty()
    text = db.TextProperty()

class ComentDB(db.Model):
    name = db.StringProperty()
    user = db.UserProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    text = db.TextProperty()