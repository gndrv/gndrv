from .cmds import list_parts, clone_part, push_part


class Gndrv(object):
    """The biological package manager"""

    def __str__(self):
        return "The biological package manager"

    def list(self):
        list_parts()

    def push(self):
        push_part()

    def clone(self, part_string):
        clone_part(part_string)
