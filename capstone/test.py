import json
import unittest

from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie


class CastingTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app)

        self.executive_producer_token = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlczdFBMUzhLeFp6dzhIbUxoUEtiQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1nZ2Voa2h5b2RjYnJpd3BxLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExNzMxNzk4OTA0MTU0OTA2NjU3MCIsImF1ZCI6IkNhc3RpbmdBZ2VuY3kiLCJpYXQiOjE3MzQxMDM2NjcsImV4cCI6MTczNDE5MDA2Nywic2NvcGUiOiIiLCJhenAiOiJPT1RNY3EyclFyUHlJWU9lN2g1cVFzMTBmcDYzbHB6aSIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvcnMiLCJhZGQ6bW92aWVzIiwiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJ1cGRhdGU6YWN0b3IiLCJ1cGRhdGU6bW92aWVzIiwidmlldzphY3RvcnMiLCJ2aWV3Om1vdmllcyJdfQ.Rtvwt4cxqueEjEyM7xDhd9UWnEX8mtiHSI3c8txGHKdvuWxRCuxdOYk8Ba9I3Wu74WUZt0BxXM3-ko6_L02rpSMg7HvAY1j16cjbaZom7eFKBugdQe-6k5rdtVJRsF_vmvmZ5eoIrDo_JsztYYAI_MrW3DQvCatoXIHcO6cSpOrHiw_pw4ZDFlMNdiKjksLXQTlEkVSpfiLiu4BOicHQCi9FLdoh6DyP7OmL_yZgex3A9Mmpq1TZHEp-lUWy3aRUokeb8JgxWge_a0roHatq0r8C14_gkCauH7DsWEgD-dKVvYmzBOgwdFmahzD8DIhFJHy5z65iVcnoAKwI-FHVDw"

        self.casting_director_token = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlczdFBMUzhLeFp6dzhIbUxoUEtiQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1nZ2Voa2h5b2RjYnJpd3BxLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNjc3OTc1NTI3OTA4NDQwNDc3MCIsImF1ZCI6IkNhc3RpbmdBZ2VuY3kiLCJpYXQiOjE3MzQxMDU2MzQsImV4cCI6MTczNDE5MjAzNCwic2NvcGUiOiIiLCJhenAiOiJPT1RNY3EyclFyUHlJWU9lN2g1cVFzMTBmcDYzbHB6aSIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvcnMiLCJkZWxldGU6YWN0b3JzIiwidXBkYXRlOmFjdG9yIiwidXBkYXRlOm1vdmllcyIsInZpZXc6YWN0b3JzIiwidmlldzptb3ZpZXMiXX0.jthan_p-0BNetM74CiFXEo9OzQJTDhFREG9rK0zvuZ1HrpoWeeXHQDPEo8niS8_Rjt5cVS-D6KZDtrT8TYescQVycKvVBnISp5QM-HiQjAvH86Zm_EGF890wQ3xIyb08RQzhNpTf0eRdjiqzXLHSvxVet3P8pSPAhTzuts14YYanWcPFN4YjtXaxstVFa1_IyRPQEn3DljJ9YyMD68YTPrf-bygZ-3gMgL41vZC4SsySm10QWPOcRfK12tiJRu4iaX0VOHMlH8S-c-wjgqYVCCxCfi1UkLVMcj959i4eekd-spF8MDXPt3JAa9HvW_KhJLPuHofnChNoAbSjLxRHsg"

        self.casting_assistant_token = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlczdFBMUzhLeFp6dzhIbUxoUEtiQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1nZ2Voa2h5b2RjYnJpd3BxLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMjUwNzg3MjYwMjA0MDIxMDQ5NCIsImF1ZCI6IkNhc3RpbmdBZ2VuY3kiLCJpYXQiOjE3MzQxMDgxMDksImV4cCI6MTczNDE5NDUwOSwic2NvcGUiOiIiLCJhenAiOiJPT1RNY3EyclFyUHlJWU9lN2g1cVFzMTBmcDYzbHB6aSIsInBlcm1pc3Npb25zIjpbInZpZXc6YWN0b3JzIiwidmlldzptb3ZpZXMiXX0.LdBi7rdDcJ-e4iwSd1n3VVFeyMs4umxyqbffbfsqJTDrIYKDtXSWSMmeX4hfOJL3Aw9Me7nl-fMKbgNJjKSrs_Ut0ZuATm5jEBFRF2WzUSE4hAxGxmdtwygM-kvKt17j8pJ8CI1nZuG0HUEtYwKJP3aDhzZ8qJxJPSeeENrkZt02yE9NTKuWpTulZK7RsGw8bCRqEDfx-r9-2pLD7qY5CHNcmmL_L6yCN-N5416sAkVakbN57M4tqBJw2jAX0BGdyHMztYA6vYIq8bx9saKbiD9p5a99r4yn7AfVSf7PCMPIGoBdy-CDLeeE0B-QcLwfLSTeTSFRogRwbVJsy2zLHQ"

        self.test_movie = {"title": "Some Movie Title", "release_year": 2020}

        self.test_actor = {
            "name": "Jane Doe",
            "age": 22,
            "gender": "female",
            "movie_id": 3,
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.drop_all()
            self.db.create_all()

    def tearDown(self):
        pass

    # GET Endpoint Tests
    # -------------------------------------------------------------------------

    # Creating a test for the /movies GET endpoint
    def test_get_movies(self):

        res = self.client().get(
            "/movies", headers={"Authorization": self.casting_assistant_token}
        )

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movies"])

    def test_get_movies_fail(self):
        res = self.client().get("/moovies")

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"], 404)
        self.assertEqual(data["message"], "Not Found")

    def test_get_actors(self):
        res = self.client().get(
            "/actors", headers={"Authorization": self.casting_director_token}
        )

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"])

    def test_get_actors_fail(self):
        res = self.client().get("/acters")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"], 404)
        self.assertEqual(data["message"], "Not Found")

    def test_add_movie_by_executive_producer(self):
        res = self.client().post(
            "/movies",
            json=self.test_movie,
            headers={"Authorization": self.executive_producer_token},
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movie_id"])

    def test_add_movie_by_casting_assistant(self):
        res = self.client().post(
            "/movies",
            json=self.test_movie,
            headers={"Authorization": self.casting_assistant_token},
        )

        self.assertEqual(res.status_code, 401)

    def test_add_movie_by_casting_director(self):
        res = self.client().post(
            "/movies",
            json=self.test_movie,
            headers={"Authorization": self.casting_director_token},
        )

        self.assertEqual(res.status_code, 401)

    def test_add_actor_casting_director(self):

        res = self.client().post(
            "/actors",
            json=self.test_actor,
            headers={"Authorization": self.casting_director_token},
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actor_id"])

    def test_add_actor_fail(self):
        res = self.client().post(
            "/actors",
            json={"name": "John Doe"},
            headers={"Authorization": self.casting_director_token},
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"], 422)
        self.assertEqual(data["message"], "Unprocessable")

    def test_add_actor_by_casting_assistant(self):

        res = self.client().post(
            "/actors",
            json=self.test_actor,
            headers={"Authorization": self.casting_assistant_token},
        )

        self.assertEqual(res.status_code, 401)

    # def test_delete_movie(self):
    #     res = self.client().delete("/movies/2")
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data["success"], True)
    #     self.assertTrue(data["deleted"])

    def test_delete_movie_fail(self):
        res = self.client().delete(
            "/movies/100000000",
            headers={"Authorization": self.executive_producer_token},
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"], 404)
        self.assertEqual(data["message"], "Not Found")

    def test_delete_actor(self):
        res = self.client().delete(
            "/actors/1",
            headers={"Authorization": self.executive_producer_token},
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["deleted"])

    def test_delete_actor_fail(self):
        res = self.client().delete(
            "/actors/100000000",
            headers={"Authorization": self.executive_producer_token},
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"], 404)
        self.assertEqual(data["message"], "Not Found")

    def test_update_movie(self):
        res = self.client().patch(
            "/movies/3",
            json={"title": "Updated movie title"},
            headers={"Authorization": self.executive_producer_token},
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movie_id"])

    def test_update_movie_fail(self):
        res = self.client().patch(
            "/movies/100000000",
            json={"title": "Updated movie title"},
            headers={"Authorization": self.casting_director_token},
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"], 404)
        self.assertEqual(data["message"], "Not Found")

    def test_update_actor(self):
        res = self.client().patch(
            "/actors/7",
            json={"name": "Updated Name"},
            headers={"Authorization": self.casting_director_token},
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actor_id"])

    def test_update_actor_fail(self):
        res = self.client().patch(
            "/actors/100000000",
            json={"name": "Updated Name"},
            headers={"Authorization": self.casting_director_token},
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"], 404)
        self.assertEqual(data["message"], "Not Found")


if __name__ == "__main__":
    unittest.main()
