from sys import maxsize


class Project:

    def __init__(self, name=None, status=None, global_cat=True, view_status=None, description=None, id=None):
        self.name = name
        self.status = status
        self.global_cat = global_cat
        self.view_status = view_status
        self.description = description
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (
                self.name is None or other.name is None or self.name == other.name)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
