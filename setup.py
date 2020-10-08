import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

version = {}
with open("shabti/version.py", "r") as fh:
    exec(fh.read(), version)

setuptools.setup(
    name="shabti",
    version=version['__version__'],
    author="Chris Wells",
    author_email="chris@cevanwells.com",
    description="An API wrapper for the Innovative Sierra API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="BSD-2-Clause",
    url="https://github.com/cevanwells/shabti",
    packages=setuptools.find_packages(exclude=['tests']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: 2-clause BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5.3',
    install_requires=[
        'requests2>=2.16.0',
        'requests-oauthlib>=1.3.0',
        'oauthlib>=3.1.0',
    ],
    extras_require={
        'dev': [
            'pytest>=6.1.1',
            'pytest-dotenv>=0.5.2',
            'vcrpy>=4.1.0'
        ]
    },
)
