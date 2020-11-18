from sys import maxsize

class Group:
    """Класс, описывающий атрибуты для метода create_group"""
    def __init__(self, name="group_name", header="group_header", footer="group_footer", id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
