from pathlib import Path

from setuptools import find_packages, setup

# The directory containing this file
HERE = Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()
DESCRIPTION = "Python library designed to be a apps for OMS Django apps."
VERSION = "0.0.0"
PACKAGE_NAME = "omni-pro-app-base"
AUTHOR = "OMNI.PRO"
AUTHOR_EMAIL = "development@omni.pro"
URL = "https://github.com/Omnipro-Solutions/saas-app-base"
INSTALL_REQUIRES = [
    "Django==5.2",
    "environs==9.5.0",
    "marshmallow==3.26.1",
    "django-jazzmin==3.0.1",
    "djangorestframework==3.14.0",
    "django-oauth-toolkit==2.3.0",
    "django-auditlog==3.1.2",
    "django-allow-cidr==0.8.0",
    "django-health-check==3.18.1",
    "django-celery-results==2.5.1",
    "django-json-widget==2.0.1",
    "django-cors-headers==4.7.0",
    "requests==2.31.0",
    "requests-oauthlib==2.0.0",
    "dj-database-url==2.3.0",
    "psycopg[binary,pool]==3.2.9",
    "whitenoise==6.6.0",
    "argon2-cffi==23.1.0",
    "celery==5.3.6",
    "redis==5.0.1",
    "django-jazzmin-admin-rangefilter==1.0.0",
    "newrelic==9.10.0",
    "django-celery-beat==2.8.1",
    "django-import-export==4.1.0",
    "django-db-connection-pool==1.2.5",
]
# with open(HERE / "requirements.txt") as f:
#     INSTALL_REQUIRES = f.read().splitlines()

# This call to setup() does all the work
setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="MIT",
    packages=find_packages(exclude=("tests",)),
    package_data={"": ["*.pyi", "data/*.csv"]},
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
    ],
    extras_require={
        "dev": [
            "pytest",
        ]
    },
    test_suite="tests",
    python_requires=">=3.11",
)
