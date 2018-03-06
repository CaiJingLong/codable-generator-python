import json

import sys

argv = sys.argv

src_path = 'src.json'
type_src = "class"
outer_name = 'Resp'

if argv.__contains__("-h"):
    print("-f [json-filename]")
    print("-o [class/or struct name]")
    print("-t [class/struct]")
    exit()

for arg in argv:
    index = argv.index(arg)
    if type(arg) is str:
        a: str = arg
        if a.startswith("-f"):
            src_path = argv[index + 1]

        if a.startswith("-t"):
            type_src = argv[index + 1]

        if a.startswith("-o"):
            outer_name = argv[index + 1]

# type
# type_src = "struct"


# default value
# show_default_value = False
show_default_value = True

file = open(src_path)
src = file.read()
# print(src)
object = json.loads(src)


class Field:
    name: str
    typeName: str
    defValue: str

    def __init__(self, name=None, type_name=None, def_value=None):
        self.name = name
        self.typeName = type_name
        self.defValue = def_value

    def __str__(self):
        result = "name = %s,typeName = %s" % (self.name, self.typeName)
        return result


def makeObject(map: dict, class_name: str = "Resp"):
    class_name = class_name[0].upper() + class_name[1:]
    field_list = list()
    for key in map.keys():
        value = map[key]
        # if (key == "status")
        if type(value) == list:
            r = makeList(value, key)
            field_list.append(Field(key, "[%s]" % r, "[]"))
        elif type(value) == dict:
            r = makeObject(value, key)
            field_list.append(Field(key, first_upper(key)))
        elif type(value) == str:
            field_list.append(Field(key, 'String', '""'))
        elif type(value) == int:
            field_list.append(Field(key, 'Int', 0))
        elif type(value) == float:
            field_list.append(Field(key, 'Float', 0.0))

    result = "%s %s: Codable{\n\n" % (type_src, class_name)
    for f in field_list:
        result += "    var %s : %s" % (f.name, f.typeName)
        if show_default_value and f.defValue is not None:
            result += " = %s" % f.defValue
        result += "\n"
    result += "\n}"

    print(result)
    return class_name


def first_upper(value: str):
    return value[0].upper() + value[1:]


def makeList(li: list, name: str):
    if len(li) == 0:
        pass

    obj = li[0]
    t = type(obj)
    if t == dict:
        obj = makeObject(obj, name)
        return obj


makeObject(object, outer_name)
