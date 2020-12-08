'''
https://github.com/mkorpusik/mealmate/blob/35dff82faa3e5c3cbdeb269e69a1cdca1b8b38bb/flask_server/load_nut_map.py
'''


class Nutrient:
    '''Class representing each nutrient.'''

    def __init__(self, nut_info):
        self.attr_id = nut_info[0]
        self.usda_tag = nut_info[1]
        self.name = nut_info[2]
        self.unit = nut_info[3]

    def __str__(self):
        return str(self.attr_id) + ' ' + str(self.name)

    def __repr__(self):
        return str(self.attr_id) + ' ' + str(self.name)


def load_table(filepath):
    '''Loads all rows in the given tsv file.'''
    with open(filepath) as infile:
        rows = [row.strip().split('\t') for row in infile]
    infile.close()
    return rows


def load_nut_map():
    '''Loads USDA nutrient info table with nutrient names and units.'''
    table = load_table('nutmap.tsv')
    nutrients = [Nutrient(r) for r in table[1:]]
    nut_map = dict(map(lambda n: [n.attr_id, n], nutrients))
    return nut_map