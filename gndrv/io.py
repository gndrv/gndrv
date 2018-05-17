import os

# TODO: use biopython


def make_part(part):
    name = part.get('name')
    desc = part.get('description')
    seq = part.get('sequence')

    if name is None:
        return

    desc_line = ' ({})'.format(desc) if desc is not None else ''

    if not os.path.exists(name):
        os.makedirs(name)

    fasta = '>{}{}\n{}'.format(name, desc_line, seq)
    with open('{}/sequence.fasta'.format(name), 'w') as f:
        f.write(fasta)


def read_part():
    with open('sequence.fasta', 'r') as f:
        fasta = f.read()
    line1, seq = fasta.split('\n', 1)
    if ' ' in line1:
        name = line1[1: line1.find(' ')]
        desc = line1[line1.find('('): line1.find(')')]
    else:
        name = line1[1:]
        desc = None
    return {'name': name, 'description': desc, 'sequence': seq}
