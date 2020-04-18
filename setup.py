import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='django-jsignature',
    version='0.9',
    author='Florent Lebreton',
    author_email='florent.lebreton@makina-corpus.com',
    url='https://github.com/fle/django-jsignature',
    download_url='http://pypi.python.org/pypi/django-jsignature',
    description='Use jSignature jQuery plugin in your django projects',
    long_description=open(os.path.join(here, 'README.rst')).read() + '\n\n' +
        open(os.path.join(here, 'CHANGES')).read(),
    license='LPGL, see LICENSE file.',
    install_requires=['Django>=1.11', 'pillow'],
    packages=find_packages(exclude=['example_project*', 'tests']),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Topic :: Utilities',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Development Status :: 5 - Production/Stable',
         'Programming Language :: Python',
         'Programming Language :: Python :: 2',
         'Programming Language :: Python :: 2.7',
         'Programming Language :: Python :: 3',
         'Programming Language :: Python :: 3.5',
         'Programming Language :: Python :: 3.6',
         'Programming Language :: Python :: 3.7',
         'Programming Language :: Python :: 3.8',
    ],
)
