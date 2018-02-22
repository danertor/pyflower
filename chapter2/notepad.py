import datetime

# Store the next available id for all notes
last_id = 0


class Note:
    """
    Represent a note in the notebook. Match against a string in searches and store tags for each note
    """

    def __init__(self, memo, tags=''):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """Determine if this note matches the filter        text. Return True if it matches, False otherwise;
        """

        return filter in self.memo or filter in self.tags


class Notebook:
    """Represent a collection of notes"""

    def __init__(self):
        # type: () -> object
        self.notes =[]

    def new_note(self, memo, tags=''):
        """Create a new note and add it to the list"""
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        """Find thenote with the given id and change its values"""
        self._find_note.memo = memo

    def modify_tag(self, note_id, tags):
        """Find a no with the given id and change its tags"""
        self._find_note.tags = tags

    def search(self, filter):
        """ Find ALL notes that match the given filter"""
        return [note for note in self.notes if note.match(filter)]

    def _find_note(self, note_id):
        """locate a note with id"""
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

