from main import db
from sqlalchemy import func

class MemberModel(db.Model):
    __tablename__="members"
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(55), nullable=False)
    lname = db.Column(db.String(55), nullable=False)
    email = db.Column(db.VARCHAR(30), nullable=False,unique=True)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())

    def create_record(self):
        db.session.add(self)
        db.session.commit()
    #fetch records
    @classmethod
    def fetch_all(cls):
        return cls.query.all()
    