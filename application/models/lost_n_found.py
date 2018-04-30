from datetime import datetime
from flask_login import current_user
from application.extensions import db
from application.models.user import User
from sqlalchemy.dialects import postgresql
from application.utils import CRUDMixin
import uuid
class LostNFoundPost(db.Model,CRUDMixin):
    id = db.Column(db.UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    author_id = db.Column(db.String, db.ForeignKey('user.id'))
    type = db.Column(db.String) # lost or found
    title = db.Column(db.String)
    category = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    content = db.Column(db.String)
    img_URLs = db.Column(postgresql.ARRAY(db.String, dimensions=1))
    place = db.Column(db.String)
    occurred_time = db.Column(db.DateTime)
    created = db.Column(db.DateTime)
    contact = db.Column(db.String)
    is_found = db.Column(db.Boolean,default=False)
    hit = db.Column(db.Integer,default=0)
    is_deleted = db.Column(db.Boolean,default=False)
    lighten_time = db.Column(db.DateTime,default=datetime.now)
    lighten_count = db.Column(db.Integer,default=0)
    

    @classmethod
    def from_json(cls,json_post):
        post = cls(
            type = json_post['type'],
            author_id = json_post['authorID'],
            title = json_post['title'],
            content = json_post['content'],
            latitude = json_post['latitude'],
            longitude = json_post['longitude'],
            img_URLs = json_post['imgURLs'],
            place = json_post['place'],
            occurred_time = datetime.fromtimestamp(json_post['occurredTime']),
            contact = json_post['contact']
        )
        return post

    def to_json(self):
        return {
            'type': self.type,
            'authorID':self.author_id,
            'title':self.title,
            'content':self.content,
            'latitude':self.latitude,
            'longitude':self.longitude,
            'imgURLs': self.img_URLs,
            'place':self.place,
            'occurredTime':self.occurred_time,
            'contact':self.contact
        }
    
    def change_found_status(self,is_founded):
        self.is_found = is_founded
        self.save()

    def lighten(self):
        self.lighten_time = datetime.now()
        self.lighten_count += 1
        self.save()
