__author__ = 'Igor Nikolaev'


class Project:
    def __init__(self, name=None, state="в разработке", globalcat=True, visible="публичный", description=None):
        self.name = name,
        self.state = state,
        self.globalcat = globalcat,
        self.visible = visible,
        self.description = description

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and (self.name is None or other.name is None or self.name == other.name)