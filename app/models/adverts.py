from datetime import datetime

from app.models import db, BaseModelMixin


class Advert(db.Model, BaseModelMixin):
    """Объявление."""

    __tablename__ = 'advertisement'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True, nullable=False)
    description = db.Column(db.Text, index=True, nullable=False, default='')
    # creator_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    created_on = db.Column(db.DateTime(), default=datetime.utcnow)

    def __str__(self):
        return f'<Advertisement {self.title}>'

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            "description": self.description,
            # 'creator_id': self.creator_id,
            'created_on': self.created_on.strftime('%d:%m:%Y')

        }