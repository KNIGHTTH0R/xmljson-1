# -*- coding: utf-8 -*-
from loadmixins import JsonMixin, XmlMixin


class XmlJson(object, JsonMixin, XmlMixin):
    """doc string"""
    def get_project(self, name):
        return self.data['projects'][name]

    def get_project_dependencies(self, name):
        return self.data['projects'][name]['dependencies']

    def get_project_version(self, name):
        return self.data['projects'][name]['version']

    def get_project_vendor(self, name):
        return self.data['projects'][name]['vendor']

    def get_projects_by_vendor(self, vendor):
        projects = []
        for key in self.data['projects']:
            if self.data['projects'][key]['vendor'] == vendor:
                projects.append(self.data['projects'][key])
        return projects
