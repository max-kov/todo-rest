from flask import Flask
from flask import jsonify, request
from notes import Notes

notes = Notes()

api = Flask(__name__)


@api.route("/", methods=["GET"])
def get_all_notes():
    return jsonify(notes.get_all())


@api.route("/<int:note_id>", methods=["GET"])
def get_note(note_id: int):
    if notes.valid_id(note_id):
        return jsonify(notes.get(note_id))


@api.route("/<int:note_id>", methods=["DELETE"])
def delete_note(note_id: int):
    if notes.valid_id(note_id):
        notes.delete(note_id)
        return jsonify(success=True)


@api.route("/", methods=["POST"])
def save_note():
    data = request.json
    notes.add(data)
    return jsonify(success=True)


@api.route("/<int:note_id>", methods=["PUT"])
def update_note(note_id: int):
    if notes.valid_id(note_id):
        data = request.json
        notes.update(note_id, data)
        return jsonify(success=True)


@api.route("/archive/<int:note_id>", methods=["PUT"])
def archive_note(note_id: int):
    if notes.valid_id(note_id):
        notes.archive(note_id)
        return jsonify(success=True)
    


api.run()
