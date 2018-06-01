from setuptools import setup

entry_points = {
    'openprocurement.api.configurator': [
        'configurator = includeme:includeme'
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
      extras_require={'test': test_requires},
      include_package_data=True,
      zip_safe=False,
      entry_points=entry_points)
