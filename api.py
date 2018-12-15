from flask import Flask

api = Flask(__name__)


@api.route("/", methods=["GET"])
def get_all_notes():
    pass


@api.route("/<int:note_id>", methods=["GET"])
def get_note(note_id: int):
    pass


@api.route("/<int:note_id>", methods=["DELETE"])
def delete_note(note_id: int):
    pass


@api.route("/", methods=["POST"])
def save_note():
    pass


@api.route("/<int:note_id>", methods=["PUT"])
def update_note(note_id: int):
    pass
