from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

# Initialize db/orm object
db = SQLAlchemy()
bcrypt = Bcrypt()
