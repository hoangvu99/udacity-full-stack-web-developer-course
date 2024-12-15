# Casting Agency Capstone Project

This is my final capstone project for Udacity's FullStack Web Developer Nanodegree.
Web app can be accessed at [here](https://castingagencyapi.onrender.com/)

##### Project Dependencies

- **Flask** - Slim python web library.
- **SQLAlchemy** - Python ORM library
- **Heroku** - PaaS platform for easy hosting of web apps
- **Postman** - API testing tool

### Installation instructions

- Clone project to directory of your choice.
- Create a virtualenv in project directory
- run `pip install -r requirements.txt` to install project dependencies
- add `DATABASE_URL` to environment variables of your system.
  On Unix systems, use `export DATABASE_URL=postgres://username:password@host:port/database_name`
- run `export FLASK_APP=app.py`
- type `flask run` in terminal

###Endpoints:

- GET /actors and /movies
- DELETE /actors/ and /movies/
- POST /actors and /movies and
- PATCH /actors/ and /movies/

### Roles

- Casting Assistant

  - GET /actors and /movies

- Casting Director
  - GET /actors and /movies
  - ADD /actors and DELETE /actors
  - PATCH /actors and /movies
- Executive Producer
  - GET /actors and /movies
  - ADD /actors and DELETE /actors
  - PATCH /actors and /movies
  - ADD /movies and DELETE /movies

### JWT Tokens for each role:

- Casting Assistant - `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlczdFBMUzhLeFp6dzhIbUxoUEtiQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1nZ2Voa2h5b2RjYnJpd3BxLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMjUwNzg3MjYwMjA0MDIxMDQ5NCIsImF1ZCI6IkNhc3RpbmdBZ2VuY3kiLCJpYXQiOjE3MzQxMDgxMDksImV4cCI6MTczNDE5NDUwOSwic2NvcGUiOiIiLCJhenAiOiJPT1RNY3EyclFyUHlJWU9lN2g1cVFzMTBmcDYzbHB6aSIsInBlcm1pc3Npb25zIjpbInZpZXc6YWN0b3JzIiwidmlldzptb3ZpZXMiXX0.LdBi7rdDcJ-e4iwSd1n3VVFeyMs4umxyqbffbfsqJTDrIYKDtXSWSMmeX4hfOJL3Aw9Me7nl-fMKbgNJjKSrs_Ut0ZuATm5jEBFRF2WzUSE4hAxGxmdtwygM-kvKt17j8pJ8CI1nZuG0HUEtYwKJP3aDhzZ8qJxJPSeeENrkZt02yE9NTKuWpTulZK7RsGw8bCRqEDfx-r9-2pLD7qY5CHNcmmL_L6yCN-N5416sAkVakbN57M4tqBJw2jAX0BGdyHMztYA6vYIq8bx9saKbiD9p5a99r4yn7AfVSf7PCMPIGoBdy-CDLeeE0B-QcLwfLSTeTSFRogRwbVJsy2zLHQ`

- Casting Director - `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlczdFBMUzhLeFp6dzhIbUxoUEtiQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1nZ2Voa2h5b2RjYnJpd3BxLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNjc3OTc1NTI3OTA4NDQwNDc3MCIsImF1ZCI6IkNhc3RpbmdBZ2VuY3kiLCJpYXQiOjE3MzQxMDU2MzQsImV4cCI6MTczNDE5MjAzNCwic2NvcGUiOiIiLCJhenAiOiJPT1RNY3EyclFyUHlJWU9lN2g1cVFzMTBmcDYzbHB6aSIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvcnMiLCJkZWxldGU6YWN0b3JzIiwidXBkYXRlOmFjdG9yIiwidXBkYXRlOm1vdmllcyIsInZpZXc6YWN0b3JzIiwidmlldzptb3ZpZXMiXX0.jthan_p-0BNetM74CiFXEo9OzQJTDhFREG9rK0zvuZ1HrpoWeeXHQDPEo8niS8_Rjt5cVS-D6KZDtrT8TYescQVycKvVBnISp5QM-HiQjAvH86Zm_EGF890wQ3xIyb08RQzhNpTf0eRdjiqzXLHSvxVet3P8pSPAhTzuts14YYanWcPFN4YjtXaxstVFa1_IyRPQEn3DljJ9YyMD68YTPrf-bygZ-3gMgL41vZC4SsySm10QWPOcRfK12tiJRu4iaX0VOHMlH8S-c-wjgqYVCCxCfi1UkLVMcj959i4eekd-spF8MDXPt3JAa9HvW_KhJLPuHofnChNoAbSjLxRHsg`

- Executive Producer - `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlczdFBMUzhLeFp6dzhIbUxoUEtiQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1nZ2Voa2h5b2RjYnJpd3BxLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExNzMxNzk4OTA0MTU0OTA2NjU3MCIsImF1ZCI6IkNhc3RpbmdBZ2VuY3kiLCJpYXQiOjE3MzQxMDM2NjcsImV4cCI6MTczNDE5MDA2Nywic2NvcGUiOiIiLCJhenAiOiJPT1RNY3EyclFyUHlJWU9lN2g1cVFzMTBmcDYzbHB6aSIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvcnMiLCJhZGQ6bW92aWVzIiwiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJ1cGRhdGU6YWN0b3IiLCJ1cGRhdGU6bW92aWVzIiwidmlldzphY3RvcnMiLCJ2aWV3Om1vdmllcyJdfQ.Rtvwt4cxqueEjEyM7xDhd9UWnEX8mtiHSI3c8txGHKdvuWxRCuxdOYk8Ba9I3Wu74WUZt0BxXM3-ko6_L02rpSMg7HvAY1j16cjbaZom7eFKBugdQe-6k5rdtVJRsF_vmvmZ5eoIrDo_JsztYYAI_MrW3DQvCatoXIHcO6cSpOrHiw_pw4ZDFlMNdiKjksLXQTlEkVSpfiLiu4BOicHQCi9FLdoh6DyP7OmL_yZgex3A9Mmpq1TZHEp-lUWy3aRUokeb8JgxWge_a0roHatq0r8C14_gkCauH7DsWEgD-dKVvYmzBOgwdFmahzD8DIhFJHy5z65iVcnoAKwI-FHVDw`

## API Endpoints

In the next few subsections, we'll cover how the API works and what you can expect back in the results.

### Default Path

#### GET /

Verifies that application is up and running on Heroku.

Sample response:

```
{
    "description": "App is running.",
    "success": true
}
```

### GET Endpoints

#### GET /movies

Displays all movies listed in the database.

Sample response:

```
{
    "movies": [
        {
            "id": 3,
            "release_year": 2008,
            "title": "Movie 3"
        },
        {
            "id": 4,
            "release_year": 1973,
            "title": "Movie 4"
        },
    ],
    "success": true
}
```

#### GET /actors

Displays all actors / actresses listed in the database.

Sample response:

```
{
    "actors": [
        {
            "age": 34,
            "gender": "female",
            "id": 3,
            "movie_id": 2,
            "name": "Actor 3"
        },
        {
            "age": 34,
            "gender": "male",
            "id": 4,
            "movie_id": 3,
            "name": "Actor 4"
        },
    ],
    "success": true
}
```

### POST Endpoints

#### POST /movies

Creates a new movie entry in the database.

Sample response:

```
{
    "movie_id": 8,
    "success": true
}
```

#### POST /actors

Creates a new actor / actress entry in the database.

Sample response:

```
{
    "actor_id": 7,
    "success": true
}
```

### PATCH Endpoints

#### PATCH /movies/<movie_id>

Updates movie information given a movie_id and newly updated attribute info.

Sample response:

```
{
    "movie_id": 2,
    "success": true
}
```

#### PATCH /actors/<actor_id>

Updates actor information given a actor_id and newly updated attribute info.

Sample response:

```
{
    "actor_id": 2,
    "success": true
}
```

### DELETE Endpoints

#### DELETE /movies/<movie_id>

Deletes a movie entry from the database given the inputted movie_id.

Sample response:

```
{
    "deleted": 1,
    "success": true
}
```

#### DELETE /movies/<actor_id>

Deletes an actor / actress entry from the database given the inputted actor_id.

Sample response:

```
{
    "deleted": 1,
    "success": true
}
```
