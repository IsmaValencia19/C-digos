#import os	

#SECRET_KEY = 'random string'
#PWD = os.path.abspath(os.curdir)	

#DEBUG = True
#SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/datos.db'.format(PWD)
SECRET_KEY = "random string"
SQLALCHEMY_DATABASE_URI = 'sqlite:///datos.sqlite3'
SQLALCHEMY_TRACK_MODIFICATIONS = False