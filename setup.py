import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='django-jsignature',
    version='0.7.6',
    author='Florent Lebreton',
    author_email='florent.lebreton@makina-corpus.com',
    url='https://github.com/makinacorpus/django-jsignature',
    download_url = "http://pypi.python.org/pypi/django-jsignature/",
    description="Use jSignature jQuery plugin in your django projects",
    long_description=open(os.path.join(here, 'README.rst')).read(),
    license='LPGL, see LICENSE file.',
    install_requires=['Django'],
    packages=find_packages(),
    include_package_data = True,
    zip_safe = False,
    classifiers  = ['Topic :: Utilities',
                    'Natural Language :: English',
                    'Operating System :: OS Independent',
                    'Intended Audience :: Developers',
                    'Environment :: Web Environment',
                    'Framework :: Django',
                    'Development Status :: 4 - Beta',
                    'Programming Language :: Python :: 2.7'],
)
