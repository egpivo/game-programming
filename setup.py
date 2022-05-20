from setuptools import find_namespace_packages, setup

setup(
    name="hello-pong",
    version="0.0.0",
    install_requires=[
        "tkinter",
    ],
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src"),
    test_suite="tests",
)
