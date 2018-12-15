class Notes:
    def __init__(self):
        self.notes = []
        self.archived = []

    def delete(self, id: int):
        self.notes.pop(id)

    def add(self, data: str):
        self.notes.append(data)

    def archive(self, id: int):
        self.archived.append(self.get(id))
        self.delete(id)

    def get_all(self):
        return self.notes

    def get(self, id: int):
        return self.notes[id]

    def update(self, id: int, data: str):
        self.notes[id] = data

    def valid_id(self, id: int):
        return 0 <= id < len(self.notes)
