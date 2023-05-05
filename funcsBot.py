def codeBlock(s: str):
    return '```' + s + '```'

def blockfy(o: object):
    s = ''
    s += 'Name: ' + str(o) + '\n'
    s += 'ID: ' + str(o.id) + '\n'
    s += 'Types: '
    for i in o.types:
        s += str(i.type.name) + ' '
    return s