from app import db
from datetime import datetime

# Create a publisher schema
class Publication(db.Model):
    __tablename__ = 'publication'

    # attributes
    id = db.Column(db.Integer, primary_key=True)  # Mandatory, must be unique
    name = db.Column(db.String(80), nullable=False)

    # init
    def __init__(self, name):
        self.name = name

    # self.id = id 		# removed because we want the id to be automatically populated

    # repr
    def __repr__(self):
        return 'Publisher is {}'.format(self.name)


# Create a book schema/class
class Book(db.Model):
    __tablename__ = 'book'

    # Columns are attributes of this class
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)  # path to bookcover image
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    # Relationships are maps to other classes
    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))

    def __init__(self, title, author, avg_rating, book_format, image, num_pages, pub_id):
        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = book_format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    # Primary keys are automatically populated by SQLAlchemy
    # We also defined pub_date to have a default

    def __repr__(self):
        return '{} by {}'.format(self.title, self.author)
