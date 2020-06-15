import os
from datetime import datetime

import pytest


def pytest_configure(config):
    if not os.path.exists('reports'):
        os.makedirs('reports')

    file_name = datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"

    module = config.option.file_or_dir

    if module is not None:
        for module_name in module:
            print("module name -> " + module_name)
            if module_name is not None and ".py" in module_name:
                report_name = module_name.split("/").pop()[:-3]
                file_name = report_name + "_" + file_name

    parameters = None

    if parameters is not None:
        for param in parameters:
            if param is not None:
                print("parameter -> " + param)
            if param is not None and ".ini" in param:
                configuration = param.split("/").pop()[:-4]
                file_name = configuration + "_" + file_name

    file_name = file_name.replace(":", "-")
    file_name = file_name.replace(" ", "-")
    config.option.htmlpath = 'reports/' + file_name


def pytest_report_header(config):
    return "Test Suite"


def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item


def pytest_runtest_setup(item):
    if "incremental" in item.keywords:
        previousfailed = getattr(item.parent, "_previousfailed", None)
        if previousfailed is not None:
            pytest.xfail("previous test failed ({})".format(previousfailed.name))
