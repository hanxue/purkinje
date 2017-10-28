from setuptools import setup


with open('README.rst') as f:
    readme = f.read()

with open('CHANGES.rst') as f:
    changes = f.read()


def parse_requirements():
    with open('requirements.txt') as req:
        return req.readlines()


setup(name='purkinje',
      version='0.1.9',
      description='Test runner for py.test with web GUI',
      long_description=readme + '\n\n' + changes,
      author='Bernhard Biskup',
      author_email='bbiskup@gmx.de',
      url='https://github.com/bbiskup/purkinje',
      package_dir={'purkinje': 'purkinje'},
      packages=['purkinje'],
      zip_safe=False,
      include_package_data=True,
      install_requires=parse_requirements(),
      entry_points={
          'console_scripts': [
              'purkinje = purkinje.purkinje:main'
          ]
      },
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Console',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development :: Testing'
      ],
      license='The MIT License (MIT)',
      keywords='purkinje pytest testrunner websockets',
      )
