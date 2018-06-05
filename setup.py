from setuptools import setup, find_packages

entry_points = {
    'openprocurement.api.configurator': [
        'configurator = openprocurement.configurator.ea2.includeme:includeme'
    ],
    'openprocurement.tests': [
        'configurator = openprocurement.configurator.ea2.tests:suite'
    ]
}
requires = [
    'openprocurement.api',
]

test_requires = requires + []

setup(name='openprocurement.configurator.ea2',
      version='0.0.1',
      description='configurator',
      classifiers=[
          "Framework :: Pylons",
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
      ],
      keywords="web services",
      author='Quintagroup, Ltd.',
      author_email='info@quintagroup.com',
      license='Apache License 2.0',
      requires=requires,
      namespace_packages=['openprocurement', 'openprocurement.configurator'],
      extras_require={'test': test_requires},
      packages=find_packages(exclude=['ez_setup']),
      include_package_data=True,
      zip_safe=False,
      entry_points=entry_points)
