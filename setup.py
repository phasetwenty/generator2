from setuptools import find_packages, setup

requires = (
    'pyramid~=1.9.1',
    'pyramid_jinja2~=2.7.0',
    'pyramid-retry~=0.5.0',
    'pyramid_tm~=2.2.0',
    'SQLAlchemy~=1.1.13',
    'zope.sqlalchemy~=0.7.7'
)

entry_points = """
[paste.app_factory]
main = generator2.server:main
[console_scripts]
initializedb = generator2.scripts.initializedb:main
getprops = generator2.scripts.getprops:main
"""

setup(
    name='generator2',
    version='0.1.0',
    package_dir={'': 'src/server'},
    packages=find_packages('src/server'),
    url='',
    license='proprietary',
    author='Christopher Haverman',
    author_email='phasetwenty@gmail.com',
    description='',
    install_requires=requires,
    entry_points=entry_points
)
