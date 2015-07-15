# -*- coding: utf-8 -*-
import json
import xmltodict
import jsonschema


SCHEMA = {
        "type": "object",
        "properties": {
            "projects": {}
        },
        "additionalProperties": False,
        "required": ["projects"]
    }


class JsonMixin():
    """Provides loading json data from file to python objects."""
    def load_json(self, path):
        with open(path) as file:
            data = json.load(file)
            jsonschema.validate(data, SCHEMA)
            self.data = data
            return data


class XmlMixin():
    """Provides loading xml data from file to python objects."""
    def load_xml(self, path):
        with open(path) as file:
            data = json.loads(json.dumps(xmltodict.parse(file)))
            jsonschema.validate(data, SCHEMA)
            self.data = data
            return data
