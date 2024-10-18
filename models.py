from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rule_string = db.Column(db.Text, nullable=False)
    ast = db.Column(db.PickleType, nullable=False)

    def __repr__(self):
        return f"<Rule {self.id}>"

