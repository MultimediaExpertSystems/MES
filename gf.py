import os
import errno
#driver code to generate data of folder after images are downloaded
def path_hierarchy(path):
    hierarchy = {
        'tags': '[' + "juventus" + ']',
        'path': './Images/' + os.path.basename(path),
    }

    try:
        hierarchy['children'] = [
            path_hierarchy(os.path.join(path, contents))
            for contents in os.listdir(path)
        ]
    except OSError as e:
        if e.errno != errno.ENOTDIR:
            raise
        h = ('file')

    return hierarchy

if __name__ == '__main__':
    import json
    import sys

    try:
        directory = sys.argv[1]
    except IndexError:
        directory = "."

    print(json.dumps(path_hierarchy(directory), indent=2, sort_keys=True))