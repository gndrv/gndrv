from .api import get_parts, get_part, post_part
from .io import make_part, read_part


def list_parts():
    parts = get_parts()

    if len(parts) == 0:
        print 'No parts'
        return

    print 'Your parts:'
    for part in parts:
        print ' - {}'.format(part.get('name'))


def clone_part(part_string):
    part_parts = part_string.split('/')
    if len(part_parts) != 2:
        print "A part is identified as [user/part_name]"
        return

    user, part_name = part_string.split('/')
    part = get_part(user, part_name)
    print 'Cloning into {}...'.format(part_name)
    make_part(part)
    print 'Done!'


def push_part():
    part = read_part()
    post_part(part)
    print 'Done!'


def config():
    pass
