import os
import unittest
import json
from flaskr import create_app
from models import db, Question, Category, setup_db
from flask_sqlalchemy import SQLAlchemy
from settings import DB_TEST_NAME, DB_USER, DB_PASSWORD


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.database_name = DB_TEST_NAME
        self.database_user = DB_USER
        self.database_password = DB_PASSWORD
        self.database_host = "localhost:5432"
        self.database_path = f"postgresql://{self.database_user}:{self.database_password}@{self.database_host}/{self.database_name}"

        # Create app with the test configuration
        self.app = create_app(
            {
                "SQLALCHEMY_DATABASE_URI": self.database_path,
                "SQLALCHEMY_TRACK_MODIFICATIONS": False,
                "TESTING": True,
            }
        )
        self.client = self.app.test_client()
        # Bind the app to the current context and create all tables
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """Executed after each test"""
        with self.app.app_context():
            db.session.remove()
            # db.drop_all()

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    """
    TEST: Endpoint GET /questions?page=1
    """

    def test_get_questions(self):
        res = self.client.get("/questions?page=1")
        question_data = json.loads(res.data)
        self.assertEqual(len(question_data["questions"]), 10)

    def test_get_questions_error(self):
        response = self.client.get("/questions?page=x")
        json_response_data = json.loads(response.data)
        self.assertEqual(response.status_code, 500)

    """
    TEST: Endpoint DELETE /questions/{question_id}
    """

    def test_delete_question_success(self):
        with self.app.app_context():
            # add new question to delete
            dummy = {
                "question": "Test delete Question?",
                "answer": "Yes this is a test question.",
                "category": 3,
                "difficulty": 2,
            }
            question = Question(**dummy)
            question.insert()
            question_to_delete = Question.query.filter_by(
                question="Test delete Question?"
            ).first()
            delete_id = question_to_delete.id
            res = self.client.delete(f"/questions/{delete_id}")
            self.assertEqual(res.status_code, 200)

    def test_delete_question_error(self):
        res = self.client.delete("/questions/random_id")
        self.assertEqual(res.status_code, 404)

    """
    TEST: Endpoint POST /questions
    """

    def test_post_new_question_success(self):
        res = self.client.post(
            "/questions",
            data=json.dumps(
                {
                    "question": "This is new question, right?",
                    "answer": "Yes this is a test question.",
                    "category": 3,
                    "difficulty": 2,
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(res.status_code, 201)

    def test_post_new_question_error(self):
        res = self.client.post(
            "/questions",
            data=json.dumps(
                {
                    "question": "This is new question, right?",
                    "answer": "Yes this is a test question.",
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(res.status_code, 400)

    """
    TEST: Endpoint POST /search_question
    """

    def test_search_question_success(self):
        res = self.client.post(
            "/search_question",
            data=json.dumps(
                {
                    "searchTerm": "Title",
                }
            ),
            content_type="application/json",
        )
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertGreaterEqual(data["totalQuestions"], 1)

    def test_search_not_found_question(self):
        res = self.client.post(
            "/search_question",
            data=json.dumps(
                {
                    "searchTerm": "random search",
                }
            ),
            content_type="application/json",
        )
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertGreaterEqual(data["totalQuestions"], 0)

    def test_search_question_error(self):
        res = self.client.post(
            "/search_question",
            data=json.dumps({}),
            content_type="application/json",
        )
        self.assertEqual(res.status_code, 500)

    """
    TEST: Endpoint GET /categories/<int:category_id>/questions
    """

    def test_get_question_by_category_success(self):
        res = self.client.get("/categories/2/questions")
        self.assertEqual(res.status_code, 200)

    def test_get_question_by_category_error(self):
        res = self.client.get("/categories/xxx/questions")
        self.assertEqual(res.status_code, 404)

    """
    TEST: Endpoint POST /quizzes
    """

    def test_get_quizzes(self):
        res = self.client.post(
            "quizzes",
            data=json.dumps({"previous_questions": [], "quiz_category": {"id": 1}}),
            content_type="application/json",
        )
        data = res.get_json()
        self.assertEqual(res.status_code, 200)

    def test_get_quizzes_error(self):
        res = self.client.post(
            "quizzes",
            data=json.dumps({}),
            content_type="application/json",
        )
        self.assertEqual(res.status_code, 500)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
