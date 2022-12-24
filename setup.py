from setuptools import setup, find_packages


with open("requirements.txt") as file:
    requirement = file.read().splitlines()

with open("README.md") as file:
    readme = file.read()


setup(
    name="send_later",
    version="1.0.0",
    author="soroosh",
    url="https://github.com/sorooshm78/send_later",
    description="send later package",
    long_description=readme,
    packages=find_packages(),
    install_requires=requirement,
    python_requires="!=3.1.*",
    entry_points={
        "console_scripts": [
            "send_later=config.main:main",
        ],
    },
)
