# todo-rest

A simple Python Flask REST API for keeping notes.

## Installation

Use `python3` with requirements in `requirements.txt`.
```
git clone https://github.com/max-kov/todo-rest.git
python3 -m venv ./.venv
source .venv/bin/activate
pip install -r requirements.txt
```

To run:
```
python3 api.py
```

## Technical details

API is written using the Flask library, because its minimal nature fits the task. On the other hand, this API might not scale too well because of python's nature to be slow.

## API overview

- Saving notes is done through a POST request. Example: `curl -i -H "Content-Type: application/json" -X POST -d '"asdf"' localhost:5000`
- Viewing notes is done through a GET request. Example: `curl -i localhost:5000/` or `curl -i localhost:5000/0` for the first note.
- Deleting notes is done through a DELETE request. Example: `curl -i -H "Content-Type: application/json" -X DELETE localhost:5000/0` to delete the first note.
- Updating notes is done through a PUT request. Example: `curl -i -H "Content-Type: application/json" -X PUT -d '"asdf"' localhost:5000/0`
- Archiving notes is done through a PUT request to the `/archive` endpoint. Example: `curl -i -H "Content-Type: application/json" -X PUT localhost:5000/archive/0`

## Conundrums

I really wanted to join the `update_note` and `archive_note` into the same endpoint. This was difficult because they both update notes, which means we have to use the "PUT" HTTP method. One solution I thought of initially was to pass keyword parameters "archive" and "edit" along with the request, but I ended up splitting those two methods in the end.

Additionally, it may make sense to split the endpoint part of the `api.py` file into a separate file, but since the file isn't too big, this isn't much of a problem.

## Improvements

Useful technology
- Database (instead of storing all data in the `Notes` class)
- Docker (for easier deployment and separation of dependancies)

Additional features
- User logins
- Display archived notes

Potential problems
- Sequential note IDs (may be bad because without restricting access to notes someone can scrape all notes just by increasing the note ID in the request)
- Security holes???
