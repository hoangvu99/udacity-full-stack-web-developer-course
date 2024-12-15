from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json

from auth import AuthError, requires_auth
from models import setup_db, Movie, Actor, create_tables


def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app, resources={r"/api/": {"origins": "*"}})

    setup_db(app)
    create_tables()

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type, Authorization, True"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET, POST, DELETE, PATCH, OPTIONS"
        )
        return response

    @app.route("/", methods=["GET"])
    def health_check():
        return jsonify({"success": True, "description": "App is running."})

    @app.route("/movies", methods=["GET"])
    @requires_auth("view:movies")
    def get_movies():
        try:
            movies = Movie.query.all()

            if not movies:
                abort(404)

            movies = [movie.format() for movie in movies]

            return jsonify({"success": True, "movies": movies})
        except Exception as error:
            print(error)
            abort(error)

    @app.route("/movies", methods=["POST"])
    @requires_auth("add:movies")
    def add_movie():
        try:
            body = request.get_json()

            title = body.get("title")
            release_year = body.get("release_year")

            if not (title and release_year):
                abort(404)

            movie = Movie(title=title, release_year=release_year)
            movie.insert()

            return jsonify({"success": True, "movie_id": movie.id})
        except Exception as error:
            abort(error)

    @app.route("/movies/<int:movie_id>", methods=["DELETE"])
    @requires_auth("delete:movies")
    def delete_movie(movie_id):
        try:
            movie = Movie.query.get(movie_id)
            movie.delete()
            return jsonify({"success": True, "deleted": movie_id})
        except Exception as error:
            abort(error)

    @app.route("/movies/<int:movie_id>", methods=["PATCH"])
    @requires_auth("update:movies")
    def update_movie(movie_id):
        movie = Movie.query.get(movie_id)

        if movie:
            try:
                body = request.get_json()

                title = body.get("title")
                release_year = body.get("release_year")
                print(body)

                if title:
                    movie.title = title
                if release_year:
                    movie.release_year = release_year

                movie.update()

                return jsonify({"success": True, "movie_id": movie.id})
            except BaseException as e:
                print(e)
                abort(422)
        else:
            abort(404)

    @app.route("/actors", methods=["GET"])
    @requires_auth("view:actors")
    def get_actors():
        actors = Actor.query.all()

        if not actors:
            abort(404)

        actors = [actor.format() for actor in actors]

        return jsonify({"success": True, "actors": actors})

    @app.route("/actors", methods=["POST"])
    @requires_auth("add:actors")
    def add_actor():
        body = request.get_json(force=True)

        name = body.get("name")
        age = body.get("age")
        gender = body.get("gender")
        movie_id = body.get("movie_id")
        print(name, age, gender, movie_id)

        if not (name and age and gender and movie_id):
            abort(422)

        try:
            actor = Actor(name=name, age=age, gender=gender, movie_id=movie_id)
            actor.insert()

            return jsonify({"success": True, "actor_id": actor.id})
        except BaseException as e:
            print(e)
            abort(422)

    @app.route("/actors/<int:actor_id>", methods=["DELETE"])
    @requires_auth("delete:actors")
    def delete_actors(actor_id):
        actor = Actor.query.get(actor_id)

        if actor:
            try:
                actor.delete()

                return jsonify({"success": True, "deleted": actor_id})
            except BaseException:
                abort(422)
        else:
            abort(404)

    @app.route("/actors/<int:actor_id>", methods=["PATCH"])
    @requires_auth("update:actor")
    def update_actors(actor_id):
        actor = Actor.query.get(actor_id)

        if actor:
            try:
                body = request.get_json()

                name = body.get("name")
                age = body.get("age")
                gender = body.get("gender")
                movie_id = body.get("movie_id")

                if name:
                    actor.name = name
                if age:
                    actor.age = age
                if gender:
                    actor.gender = gender
                if movie_id:
                    actor.movie_id = movie_id

                actor.update()

                return jsonify({"success": True, "actor_id": actor.id})

            except BaseException:
                abort(422)

        else:
            abort(404)

    @app.errorhandler(422)
    def unprocessable(error):
        return (
            jsonify({"success": False, "error": 422, "message": "Unprocessable"}),
            422,
        )

    @app.errorhandler(400)
    def unprocessable(error):
        return (
            jsonify({"success": False, "error": 400, "message": "Bad Request"}),
            400,
        )

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"success": False, "error": 404, "message": "Not Found"}), 404

    @app.errorhandler(500)
    def not_found(error):
        return (
            jsonify(
                {"success": False, "error": 500, "message": "Internal Server Error"}
            ),
            500,
        )

    @app.errorhandler(AuthError)
    def handle_auth_errors(x):
        return (
            jsonify({"success": False, "error": x.status_code, "message": x.error}),
            401,
        )

    return app


app = create_app()

if __name__ == "__main__":
    app.run(port=8080, debug=True)
