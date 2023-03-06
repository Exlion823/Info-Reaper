from setuptools import setup, find_packages

setup(
    name="info",
    version="0.1",
    description="Allows you to gather Some Information about your pc",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["info=info.main"]
    },
    author="Vbuuu, iLvkii",
    license="Custom"
)
