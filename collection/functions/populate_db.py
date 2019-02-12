from collection.models import Object_types, Attribute
import json


def clear_object_hierachy_tree():
    Object_types.objects.all().delete()


def clear_attributes():
    Attribute.objects.all().delete()




def populate_object_hierachy_tree():
    # records = [{"id":"n1", "text" : "Thing", "li_attr": {}, "parent":"#"}, {"id":"n2", "text" : "Object" , "li_attr": {}, "parent":"n1"}, {"id":"n3", "text": "Living thing", "li_attr": {}, "parent":"n2"}, {"id":"n4", "text": "Plant", "li_attr": {"attribute_values": [{"attribute":"Kingdom",                    "operation":"=", "value":"Plantae"}, {"attribute":"Does photosynthesis",                    "operation":"=", "value":True } ] }, "a_attr":{"scientific":["Plantae"]}, "parent":"n3"}, {"id":"n5", "text":"Tree", "li_attr": {"attribute_values": [{"attribute":"Has woody tissue",                    "operation":"=", "value":True}, { "attribute":"Age",                   "operation":"<", "value":"7000"}]},  "parent":"n4"}, {"id":"n6", "text": "Oak", "li_attr": {"attribute_values": [{"attribute":"Produces nuts",                    "operation": "=", "value":True}, { "attribute":"Has leaves",                    "operation":"=", "value":True }, {"attribute":"Age",                   "operation":"<", "value":"700"}, {"attribute":"Age",                   "operation": "<", "value":"100"}, { "attribute":"Weight",                    "operation":"<", "value":"9000" } ] }, "a_attr":{ "synonyms": ["oak tree"], "scientific": ["Quercus"]}, "parent":"n5"}, {"id":"n7", "text": "Chestnut", "li_attr": {"attribute_values": [{"attribute":"Produces nuts",                    "operation":"=", "value":True }, { "attribute":"Produces berries",                    "operation":"=", "value":False }, { "attribute":"Age",                   "operation":"<", "value":"400"}, {"attribute":"Height",                   "operation":"<", "value":"130"}, {"attribute":"Weight",                    "operation":"<", "value":"10000"}]}, "a_attr":{"scientific": ["Castanea"]}, "parent":"n5" }, {"id":"n8", "text": "Flower", "li_attr": {"attribute_values": [{"attribute":"Has petals",                    "operation":"=", "value":True } ] }, "parent":"n4"}, {"id":"n9", "text":"Lily", "li_attr": {"attribute_values": [{"attribute":"Petal color",                    "operation":"=", "value":"yellow"}]}, "parent":"n8"}, {"id":"n10", "text":"Animal", "li_attr": {"attribute_values": [{"attribute":"Kingdom",                    "operation": "=", "value":"Animalia"}]}, "a_attr":{"synonyms": ["Creature"], "scientific": ["Animalia"]}, "parent":"n2"} ]
    # records = [{"id":"n1", "text" : "Thing", "li_attr": {}, "parent":"#"}, {"id":"n2", "text" : "Object" , "li_attr": {}, "parent":"n1"}, {"id":"n3", "text": "Living thing", "li_attr": {}, "parent":"n2"}, {"id":"n4", "text": "Plant", "li_attr": {"attribute_values": [{"attribute":"Kingdom", "attribute_id":11, "operation":"=", "value":"Plantae"}, {"attribute":"Does photosynthesis", "attribute_id":12, "operation":"=", "value":True } ] }, "a_attr":{"scientific":["Plantae"]}, "parent":"n3"}, {"id":"n5", "text":"Tree", "li_attr": {"attribute_values": [{"attribute":"Has woody tissue", "attribute_id":13, "operation":"=", "value":True}, { "attribute":"Age", "attribute_id":8, "operation":"<", "value":"7000"}]},  "parent":"n4"}, {"id":"n6", "text": "Oak", "li_attr": {"attribute_values": [{"attribute":"Produces nuts", "attribute_id":14, "operation":"=", "value":True }, { "attribute":"Has leaves", "attribute_id":15, "operation":"=", "value":True }, {"attribute":"Age", "attribute_id":8, "operation":"<", "value":"700"}, {"attribute":"Age", "attribute_id":8, "operation":"<", "value":"100" }, { "attribute":"Weight", "attribute_id":16, "operation":"<", "value":"9000" } ] }, "a_attr":{ "synonyms": ["oak tree"], "scientific": ["Quercus"]}, "parent":"n5"}, {"id":"n7", "text": "Chestnut", "li_attr": {"attribute_values": [{"attribute":"Produces nuts", "attribute_id":14, "operation":"=", "value":True }, { "attribute":"Produces berries", "attribute_id":17, "operation":"=", "value":False }, { "attribute":"Age", "attribute_id":8, "operation":"<", "value":"400"}, {"attribute":"Height", "attribute_id":18, "operation":"<", "value":"130"}, {"attribute":"Weight", "attribute_id":16, "operation":"<", "value":"10000"}]}, "a_attr":{ "scientific":["Castanea"]}, "parent":"n5" }, {"id":"n8", "text": "Flower", "li_attr": {"attribute_values": [{"attribute":"Has petals", "attribute_id":19, "operation":"=", "value":True } ] }, "parent":"n4"}, {"id":"n9", "text":"Lily", "li_attr": {"attribute_values": [{"attribute":"Petal color", "attribute_id":20, "operation":"=", "value":"yellow"}]}, "parent":"n8"}, {"id":"n10", "text":"Animal", "li_attr": {"attribute_values": [{"attribute":"Kingdom", "attribute_id":11, "operation": "=", "value":"Animalia"}]}, "a_attr":{"synonyms": ["Creature"], "scientific": ["Animalia"]}, "parent":"n2"} ]
    records = [ { "id":"n1", "text":"Thing", "li_attr":{  }, "parent":"#" }, { "id":"n2", "text":"Object", "li_attr":{  }, "parent":"n1" }, { "id":"n3", "text":"Living thing", "li_attr":{  }, "parent":"n2" }, { "id":"n4", "text":"Plant", "li_attr":{ "attribute_values":[ { "attribute":"Kingdom", "attribute_id":11, "operation":"=", "value":"Plantae" }, { "attribute":"Does photosynthesis", "attribute_id":12, "operation":"=", "value":True } ] }, "a_attr":{ "scientific":[ "Plantae" ] }, "parent":"n3" }, { "id":"n5", "text":"Tree", "li_attr":{ "attribute_values":[ { "attribute":"Has woody tissue", "attribute_id":13, "operation":"=", "value":True }, { "attribute":"Age", "attribute_id":8, "operation":"<", "value":7000 } ] }, "parent":"n4" }, { "id":"n6", "text":"Oak", "li_attr":{ "attribute_values":[ { "attribute":"Produces nuts", "attribute_id":14, "operation":"=", "value":True }, { "attribute":"Has leaves", "attribute_id":15, "operation":"=", "value":True }, { "attribute":"Age", "attribute_id":8, "operation":"<", "value":700 }, { "attribute":"Age", "attribute_id":8, "operation":"<", "value":100 }, { "attribute":"Weight", "attribute_id":16, "operation":"<", "value":9000 } ] }, "a_attr":{ "synonyms":[ "oak tree" ], "scientific":[ "Quercus" ] }, "parent":"n5" }, { "id":"n7", "text":"Chestnut", "li_attr":{ "attribute_values":[ { "attribute":"Produces nuts", "attribute_id":14, "operation":"=", "value":True }, { "attribute":"Produces berries", "attribute_id":17, "operation":"=", "value":False }, { "attribute":"Age", "attribute_id":8, "operation":"<", "value":400 }, { "attribute":"Height", "attribute_id":18, "operation":"<", "value":130 }, { "attribute":"Weight", "attribute_id":16, "operation":"<", "value":10000 } ] }, "a_attr":{ "scientific":[ "Castanea" ] }, "parent":"n5" }, { "id":"n8", "text":"Flower", "li_attr":{ "attribute_values":[ { "attribute":"Has petals", "attribute_id":19, "operation":"=", "value":True } ] }, "parent":"n4" }, { "id":"n9", "text":"Lily", "li_attr":{ "attribute_values":[ { "attribute":"Petal color", "attribute_id":20, "operation":"=", "value":"yellow" } ] }, "parent":"n8" }, { "id":"n10", "text":"Animal", "li_attr":{ "attribute_values":[ { "attribute":"Kingdom", "attribute_id":11, "operation":"=", "value":"Animalia" } ] }, "a_attr":{ "synonyms":[ "Creature" ], "scientific":[ "Animalia" ] }, "parent":"n2" } ]
    for record in records:
        if isinstance(record,dict):
            obj_type_record = Object_types(id=record.get('id'), parent=record.get('parent'), name=record.get('text'), li_attr=json.dumps(record.get('li_attr')), a_attr=json.dumps(record.get('a_attr')),)
            obj_type_record.save()

def populate_attributes():
    attributes = [{"attribute_name": "Country", "attribute_id": 1, "description": "this is a good option", "format_specification": {"fields": {"column": {"type": "string", "min_length": 4, "max_length": 52, "max_nulls": 10000}}}, "first_applicable_object": "n1"}, {"attribute_name": "Year", "attribute_id": 2, "description": "this is a good option", "format_specification": {"fields": {"column": {"type": "int", "min": 1995, "max": 2011, "sign": "positive", "max_nulls": 10000}}}, "first_applicable_object": "n1"}, {"attribute_name": "Count", "attribute_id": 3, "description": "this is a good option", "format_specification": {"fields": {"column": {"type": "int", "min": 0, "max": 45559, "sign": "non-negative", "max_nulls": 10000}}}, "first_applicable_object": "n1"}, {"attribute_name": "Rate", "attribute_id": 4, "description": "this is a good option", "format_specification": {"fields": {"column": {"type": "real", "min": 0.0, "max": 139.1, "sign": "non-negative", "max_nulls": 10000}}}, "first_applicable_object": "n1"}, {"attribute_name": "Source", "attribute_id": 5, "description": "this is a good option", "format_specification": {"fields": {"column": {"type": "string", "min_length": 3, "max_length": 28, "max_nulls": 10000}}}, "first_applicable_object": "n1"}, {"attribute_name": "Source Type", "attribute_id": 6, "description": "this is a good option", "format_specification": {"fields": {"column": {"type": "string", "min_length": 2, "max_length": 2, "max_nulls": 10000, "allowed_values": ["CJ", "PH"]}}}, "first_applicable_object": "n1"}, {"attribute_name": "Leaf Coverage", "attribute_id": 7, "description": "The percentage of the ground that is in shadow when the sun is shining from directly above.", "format_specification": {"fields": {"column": {"type": "real", "min":0.0, "max":1.0}}}, "first_applicable_object": "n1"}, {"attribute_name": "Age", "attribute_id": 8, "description": "number of years in existence", "format_specification": {"fields": {"column": {"type": "int", "min": 0, "max": 1000000}}}, "first_applicable_object": "n1"}, {"attribute_name": "New Test Attribute", "attribute_id": 9, "description": "some description", "format_specification": {"fields": {"column": {"type": "int", "min": 4, "max": 34}}}, "first_applicable_object": "n1"}, {"attribute_name": "test attribute 123", "attribute_id": 10, "description": "slkfskl", "format_specification": {"fields": {"column": {"type": "string", "min_length": 2, "max_length": 6}}}, "first_applicable_object": "n1"}, {"attribute_name": "Kingdom", "attribute_id": 11, "description": "animal kingdom", "format_specification": {"fields": {"column": {"type": "string", "min_length": 2, "max_length": 20}}}, "first_applicable_object": "n1"}, {"attribute_name": "Does photosynthesis", "attribute_id": 12, "description": "", "format_specification": {"fields": {"column": {"type": "bool"}}}, "first_applicable_object": "n1"}, {"attribute_name": "Has woody tissue", "attribute_id": 13, "description": "", "format_specification": {"fields": {"column": {"type": "bool"}}}, "first_applicable_object": "n1"}, {"attribute_name": "Produces nuts", "attribute_id": 14, "description": "", "format_specification": {"fields": {"column": {"type": "bool"}}}, "first_applicable_object": "n1"}, {"attribute_name": "Has leaves", "attribute_id": 15, "description": "", "format_specification": {"fields": {"column": {"type": "bool"}}}, "first_applicable_object": "n1"}, {"attribute_name": "Weight", "attribute_id": 16, "description": "in kg", "format_specification": {"fields": {"column": {"type": "real", "min": 0.0, "max": 1000000000000000.0}}}, "first_applicable_object": "n1"}, {"attribute_name": "Produces berries", "attribute_id": 17, "description": "", "format_specification": {"fields": {"column": {"type": "bool"}}}, "first_applicable_object": "n1"}, {"attribute_name": "Height", "attribute_id": 18, "description": "in m", "format_specification": {"fields": {"column": {"type": "real", "min": 0.0, "max": 1000000000000000.0}}}, "first_applicable_object": "n1"}, {"attribute_name": "Has petals", "attribute_id": 19, "description": "", "format_specification": {"fields": {"column": {"type": "bool"}}}, "first_applicable_object": "n1"}, {"attribute_name": "Petal color", "attribute_id": 20, "description": "", "format_specification": {"fields": {"column": {"type": "string", "min_length": 2, "max_length": 20}}}, "first_applicable_object": "n1"}]
    for attribute in attributes:
        attribute_record = Attribute(id=attribute['attribute_id'], name=attribute['attribute_name'], description=attribute['description'], format_specification=json.dumps(attribute['format_specification']), first_applicable_object=attribute['first_applicable_object'], )
        attribute_record.save()


