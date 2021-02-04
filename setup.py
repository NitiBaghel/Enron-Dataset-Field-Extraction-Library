from setuptools import find_packages, setup
setup(
    name='extractenronlib',
    packages=find_packages(include=['extractenronlib']),
    version='0.1.0',
    description='Enron dataset field extration library',
    author='Niti Baghel',
    license='MIT',
    install_requires=['pandas'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='test',
)