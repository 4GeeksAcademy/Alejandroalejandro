from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import app
from models import db, User, Post, Comment, Media

admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap4')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Comment, db.session))
admin.add_view(ModelView(Media, db.session))