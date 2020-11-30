from setuptools_scm import get_version
from flit_core import buildapi

get_version(
    write_to="demo/_version.py",
    fallback_version="0.0.0",
)
