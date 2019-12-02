from models import db, Post, Comment

posts = db.session.query(Post).all()
for p in posts:
    p.permalink = p.permalink.replace('/r/', '/i/')
    db.session.add(p)
comments = db.session.query(Comment).all()
for c in comments:
    c.permalink = c.permalink.replace('/r/', '/i/')
    db.session.add(c)
db.session.commit()