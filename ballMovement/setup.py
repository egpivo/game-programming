from setuptools import find_namespace_packages, setup

setup(
    name="ball-movement",
    version="0.0.0",
    install_requires=[
        "cocos2d"
    ],
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src"),
    test_suite="tests",
)
