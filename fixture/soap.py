__author__ = 'Igor Nikolaev'
from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper():
    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self, username, password):
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        project_list = []
        try:
            projects = client.service.mc_projects_get_user_accessible(username, password)
            for project in projects:
                project_list.append(Project(name=project.name, id=project.id))
            return project_list
        except WebFault:
            return False
