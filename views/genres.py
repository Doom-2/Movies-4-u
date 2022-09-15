from flask import request
from flask_restx import Resource, Namespace
from dao.model.genre import GenreSchema
from container import genre_service
from helpers.decorators import auth_required, admin_required

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):

    @auth_required
    def get(self):
        all_genres = genre_service.get_all()
        response = genres_schema.dump(all_genres)
        return response, 200

    @admin_required
    def post(self):
        request_json = request.json
        new_genre = genre_service.create(request_json)
        return "", 201, {"location": f"/genres/{new_genre.id}"}


@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):

    @auth_required
    def get(self, genre_id):
        single_genre = genre_service.get_one(genre_id)
        response = genres_schema.dump(single_genre)
        return response, 200

    @admin_required
    def put(self, genre_id: int):
        request_json = request.json
        request_json["id"] = genre_id
        genre_service.update(request_json)
        return "", 204

    @admin_required
    def delete(self, genre_id: int):
        genre_service.delete(genre_id)
        return "", 204
