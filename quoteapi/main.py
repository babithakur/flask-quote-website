from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class QuoteModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"Video(quote = {quote})"

#db.create_all()

resource_fields = {
    'id': fields.Integer,
    'quote': fields.String
}

class Quote(Resource):

    @marshal_with(resource_fields)
    def get(self, qid):
        result = QuoteModel.query.filter_by(id=qid).first()
        if not result:
            abort(404, message="Couldn't find quote with that id!")
        return result

q = QuoteModel(quote='My another computer, is your computer!')
db.session.add(q)
db.session.commit()
api.add_resource(Quote, "/<int:qid>")
if __name__ == '__main__':
    app.run(debug=True, port=8000)