from setuptools import Extension, setup

setup(
    name="fibonacci",
    ext_modules=[
        Extension("fibonacci", ["fibonacci.c"]),
    ],
)
