from setuptools import find_packages, setup

install_requires = [
    "termcolor>=1.1.0",
]


# as of Python >= 2.7 argparse module is maintained within Python.
extras_require = {
    ':python_version in "2.4, 2.5, 2.6"': ["argparse>=1.1.0"],
}


setup(
    name="gcplogs",
    version="0.1.0",
    url="https://github.com/zeyaddeeb/gcplogs",
    license="BSD",
    author="Zeyad Deeb",
    author_email="zeyad.deeb@icloud.com",
    description="gcplogs is a simple command line tool to read gcp logs.",
    long_description="gcplogs is a simple command line tool to read gcp logs.",
    keywords="gcp logs",
    packages=find_packages(),
    platforms="any",
    install_requires=install_requires,
    extras_require=extras_require,
    test_suite="tests",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
    entry_points={"console_scripts": ["gcplogs = gcplogs.bin:main",]},
    zip_safe=False,
)
