from datetime import datetime

from share import db
import config

iuser_username_fk = db.ForeignKey('iuser.username')
iuser_id_fk = db.ForeignKey('iuser.id')
topic_id_fk = db.ForeignKey('topic.id')
idea_id_fk = db.ForeignKey('idea.id')
stance_id_fk = db.ForeignKey('stance.id')


class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shortname = db.Column(db.String(30), unique=True, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    created_by = db.Column(db.Integer, iuser_username_fk, nullable=False)
    created_by_id = db.Column(db.Integer, iuser_id_fk, nullable=False)
    scheme = db.Column(db.String(20), nullable=False)
    created = db.Column(db.DateTime, default=datetime.now, nullable=False)
    description = db.Column(db.String(20000), nullable=True, default=None)
    css = db.Column(db.String(20000), default=None)

    def get_stances(self, deleted=False, count=False):
        if count:
            return db.session.query(Stance).filter_by(sub=self.name, deleted=deleted).count()
        return db.session.query(Stance).filter_by(sub=self.name, deleted=deleted)

    def __repr__(self):
        return f'<Topic id={self.id}, shortname={self.shortname}>'


class Stance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(2000), nullable=False)
    premises = db.Column(db.ARRAY(db.Integer))
    conclusion = db.Column(db.Integer, idea_id_fk)
    created = db.Column(db.DateTime, default=datetime.now, nullable=False)
    author = db.Column(db.String(20), iuser_username_fk, nullable=False)
    author_id = db.Column(db.Integer, iuser_id_fk, nullable=False)
    topic_id = db.Column(db.Integer, topic_id_fk)

    def get_ideas(self):
        for key in self.premises:
            yield db.session.query(Idea).filber_by(id=key)
        yield db.session.query(Idea).filber_by(id=self.conclusion)


class Idea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(2000), nullable=False)
    text = db.Column(db.String(500), nullable=False)
    conclusion_of = db.Column(db.Integer, stance_id_fk, nullable=True)
    stances_used_in = db.Column(db.ARRAY(db.Integer), nullable=True)
    created = db.Column(db.DateTime, default=datetime.now, nullable=False)
    author = db.Column(db.String(20), iuser_username_fk, nullable=False)
    author_id = db.Column(db.Integer, iuser_id_fk, nullable=False)
