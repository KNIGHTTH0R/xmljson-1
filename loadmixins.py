# -*- coding: utf-8 -*-
import json
import xmltodict
import jsonschema
from lxml import etree


class JsonMixin(object):
    """Provides loading json data from file to python objects."""
    schema = {
        "type": "object",
        "properties": {
            "projects": {}
        },
        "additionalProperties": False,
        "required": ["projects"]
    }

    def load_json(self, path):
        data = json.load(open(path))

        try:
            jsonschema.validate(data, self.schema)
        except jsonschema.SchemaError as e:
            print e
            exit(1)

        self.data = data
        return data


class XmlMixin(object):
    """Provides loading xml data from file to python objects."""
    def load_xml(self, path):
        schema_doc = etree.parse('data.xsd')

        try:
            schema = etree.XMLSchema(schema_doc)
        except etree.XMLSchemaParseError as e:
            print e
            exit(1)

        try:
            schema.assertValid(etree.parse(path))
        except etree.DocumentInvalid as e:
            print e
            exit(1)

        xml_file = open(path)
        data = xmltodict.parse(xml_file)
        self.data = data
        return data
