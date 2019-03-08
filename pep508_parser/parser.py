#!/usr/bin/env python3

import parsley
import os
import platform
import sys
import copy
from pep508_parser import grammar

PARSER = None


def format_full_version(info):
    version = "{0.major}.{0.minor}.{0.micro}".format(info)
    kind = info.releaselevel
    if kind != "final":
        version += kind[0] + str(info.serial)
    return version


if hasattr(sys, "implementation"):
    implementation_version = format_full_version(sys.implementation.version)
    implementation_name = sys.implementation.name
else:
    implementation_version = "0"
    implementation_name = ""

DEFAULT_BINDINGS = {
    "implementation_name": implementation_name,
    "implementation_version": implementation_version,
    "os_name": os.name,
    "platform_machine": platform.machine(),
    "platform_python_implementation": platform.python_implementation(),
    "platform_release": platform.release(),
    "platform_system": platform.system(),
    "platform_version": platform.version(),
    "python_full_version": platform.python_version(),
    "python_version": platform.python_version()[:3],
    "sys_platform": sys.platform,
    "extra": "",
}


def parse(s, extra=None, bindings=None):
    if not bindings:
        bindings = copy.deepcopy(DEFAULT_BINDINGS)
    if extra:
        bindings["extra"] = extra

    global PARSER
    if not PARSER:
        PARSER = parsley.makeGrammar(grammar.GRAMMAR, {"lookup": bindings.__getitem__})

    return PARSER(s).specification()
