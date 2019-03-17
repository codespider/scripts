from setuptools import setup, find_packages

install_requires = [
    'parse==1.11.1',
]

setup(
    name='repo',
    version='0.1',
    description='repo organizer',
    long_description='repo organizer',
    url='https://github.com/codespider/scripts',
    author='codespider',
    author_email='karthikkannan@gmail.com',
    license='BSD',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'repo1 = repo.commands:main',
        ],
    },
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development',
        'Topic :: Terminals',
        'Topic :: Utilities'
    ],
)
