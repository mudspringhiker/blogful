import os
class DevelopmentConfig(object):
	SQLALCHEMY_DATABASE_URI = "postgresql://localhost/blogful"
	DEBUG = True