from setuptools import setup, find_packages


with open("requirements.txt") as file:
    requirement = file.read().splitlines()


setup(
    name="send_later",
    version="1.0.0",
    author="soroosh",
    url="https://github.com/sorooshm78/send_later",
    description="send later package",
    packages=find_packages(),
    install_requires=requirement,
    entry_points={
        "console_scripts": [
            "send_later=send_later.main:main",
        ],
    },
)
