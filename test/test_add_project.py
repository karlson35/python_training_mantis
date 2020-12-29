__author__ = 'Igor Nikolaev'

from model.project import Project
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app):
    app.session.ensure_login("administrator", "root")
    status = random.choice(["development", "release", "stable", "obsolete"])
    view_status = random.choice(["public", "private"])
    project = Project(name=random_string("test", 10), status=status, view_status=view_status,
                      description="test")
    old_projects = app.soap.get_projects_list("administrator", "root")
    app.project.create_new_project(project)
    new_projects = app.soap.get_projects_list("administrator", "root")
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
