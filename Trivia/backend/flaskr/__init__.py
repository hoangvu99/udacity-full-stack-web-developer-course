from flask import Flask, request, abort, jsonify
from flask_cors import CORS
import random
import logging
from models import setup_db, Question, Category, db

QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    if test_config is None:
        setup_db(app)
    else:
        database_path = test_config.get("SQLALCHEMY_DATABASE_URI")
        setup_db(app, database_path=database_path)

    """
    @DONE: Set up CORS. Allow '*' for origins. Delete the sample route after completing the DONEs
    """
    CORS(app, resources={r"/*": {"origins": "*"}})
    with app.app_context():
        db.create_all()

    """
    @DONE: Use the after_request decorator to set Access-Control-Allow
    """

    @app.after_request
    def set_response_headers(response):
        response.headers["Access-Control-Allow-Origin"] = "*"
        return response

    """
    @DONE:
    Create an endpoint to handle GET requests
    for all available categories.
    """

    @app.route("/categories", methods=["GET"])
    def get_categories():
        try:
            query_categories = Category.query.all()
            categories_dict = {}
            for row in query_categories:
                categories_dict[row.id] = row.type
            return jsonify({"categories": categories_dict})
        except Exception as error:
            abort(500)

    """
    @DONE:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """

    @app.route("/questions", methods=["GET"])
    def get_questions():
        try:
            page = int(request.args.get("page")) - 1

            question_query = Question.query
            question_count = question_query.count()
            if page * QUESTIONS_PER_PAGE > question_count:
                raise Exception(404)
            query_categories = Category.query.all()
            categories_dict = {}
            for row in query_categories:
                categories_dict[row.id] = row.type

            questions = []
            for row in question_query.limit(QUESTIONS_PER_PAGE).offset(
                page * QUESTIONS_PER_PAGE
            ):
                questions.append(row.format())

            return jsonify(
                {
                    "questions": questions,
                    "total_questions": question_count,
                    "current_category": "",
                    "categories": categories_dict,
                }
            )
        except ValueError as value_error:
            print(value_error)
        except Exception as error:
            abort(error)

    """
    @DONE:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """

    @app.route("/questions/<int:question_id>", methods=["DELETE"])
    def delete_question(question_id):
        try:
            question_to_delete = Question.query.get(question_id)

            if question_to_delete is None:
                raise Exception(404)

            Question.delete(question_to_delete)
            return jsonify({"success": True, "deleted": question_id})
        except Exception as error:
            abort(error)

    """
    @DONE:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """

    @app.route("/questions", methods=["POST"])
    def post_question():

        try:
            body = request.get_json()

            data = {
                "question": body["question"],
                "answer": body["answer"],
                "category": body["category"],
                "difficulty": body["difficulty"],
            }
        except:
            abort(400)

        try:
            question = Question(**data)
            question.insert()
            return jsonify(success=True), 201
        except:
            return jsonify(success=False), 500

    """
    @DONE:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """

    @app.route("/search_question", methods=["POST"])
    def search_question():
        try:
            body = request.get_json()
            search_term = body["searchTerm"]

            search_query = Question.query.filter(
                Question.question.ilike("%" + search_term + "%")
            ).all()
            questions = []
            for row in search_query:
                questions.append(row.format())
            return jsonify(
                {
                    "questions": questions,
                    "totalQuestions": len(questions),
                    "currentCategory": "",
                }
            )
        except Exception as error:
            abort(error)

    """
    @DONE:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """

    @app.route("/categories/<int:category_id>/questions", methods=["GET"])
    def get_questions_by_category(category_id):
        try:
            search_query = Question.query.filter(Question.category == category_id).all()
            questions = []
            for row in search_query:
                questions.append(row.format())
            return jsonify(
                {
                    "questions": questions,
                    "totalQuestions": len(questions),
                    "currentCategory": "",
                }
            )
        except Exception as error:
            abort(error)

    """
    @DONE:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """

    @app.route("/quizzes", methods=["POST"])
    def get_quizzes():
        try:
            body = request.get_json()
            previous_questions = body["previous_questions"]
            quiz_category = body["quiz_category"]
            quiz_category_id = quiz_category["id"]
            if quiz_category_id == 0:
                filtered_question = Question.query.filter(
                    Question.id.not_in(previous_questions),
                ).first()
            else:
                filtered_question = Question.query.filter(
                    Question.id.not_in(previous_questions),
                    Question.category == quiz_category_id,
                ).first()
            app.logger.error("log here", filtered_question)
            return jsonify(
                {
                    "question": (
                        filtered_question.format()
                        if filtered_question is not None
                        else None
                    )
                }
            )
        except KeyError as key_error:
            print("errorrrr", key_error)

            abort(key_error)
        except Exception as error:
            app.logger.error("error here", error)
            abort(error)

    """
    @DONE:
    Create error handlers for all expected errors
    including 404 and 422.
    """

    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 404, "message": "Resource Not found"}),
            404,
        )

    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({"success": False, "error": 405, "message": "Not Allowed"}), 405

    @app.errorhandler(422)
    def unprocessable(error):
        return (
            jsonify({"success": False, "error": 422, "message": "Unprocessable"}),
            422,
        )

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"success": False, "error": 400, "message": "Bad Request"}), 400

    @app.errorhandler(500)
    def internal_server_error(error):
        return (
            jsonify(
                {"success": False, "error": 400, "message": "Internal Server Error"}
            ),
            500,
        )

    return app
