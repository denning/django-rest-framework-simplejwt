#!/usr/bin/env python
from distutils.core import setup

extras_require = {
    'test': [
        'cryptography',
        'pytest-cov',
        'pytest-django',
        'pytest-xdist',
        'pytest',
        'tox',
    ],
    'lint': [
        'flake8',
        'pep8',
        'isort',
    ],
    'doc': [
        'Sphinx>=1.6.5,<2',
        'sphinx_rtd_theme>=0.1.9',
    ],
    'dev': [
        'bumpversion>=0.5.3,<1',
        'pytest-watch',
        'wheel',
        'twine',
        'ipython',
    ],
    'python-jose': [
        'python-jose==3.0.0',
    ],
}

extras_require['dev'] = (
    extras_require['dev'] +  # noqa: W504
    extras_require['test'] +  # noqa: W504
    extras_require['lint'] +  # noqa: W504
    extras_require['doc'] +  # noqa: W504
    extras_require['python-jose']
)


setup(
    name='djangorestframework_simplejwt',
    version='4.4.0',
    url='https://github.com/SimpleJWT/django-rest-framework-simplejwt',
    license='MIT',
    description='A minimal JSON Web Token authentication plugin for Django REST Framework',
    long_description=open('README.rst', 'r', encoding='utf-8').read(),
    author='David Sanders',
    author_email='davesque@gmail.com',
    install_requires=[
        'django',
        'djangorestframework',
        'pyjwt',
    ],
    python_requires='>=3.6',
    extras_require=extras_require,
    packages=['rest_framework_simplejwt'],
    package_data={
        'rest_framework_simplejwt': [
            'locale/*/LC_MESSAGES/django.po',
            'locale/*/LC_MESSAGES/django.mo',
        ],
    },
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
