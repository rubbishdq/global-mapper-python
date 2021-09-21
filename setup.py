import sys

from skbuild import setup

# Require pytest-runner only when running tests
pytest_runner = (['pytest-runner>=2.0,<3dev']
                 if any(arg in sys.argv for arg in ('pytest', 'test'))
                 else [])

setup_requires = pytest_runner

setup(
    name="global-mapper-python",
    version="1.0.0",
    description="global mapper from acl-mapping (python version)",
    author='dqs',
    license="MIT",
    packages=['pyglmp'],
    install_requires=['cython'],
    tests_require=['pytest'],
    setup_requires=setup_requires
)
