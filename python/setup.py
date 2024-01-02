#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

requirements = [
    "Click>=7.0",
    "openai>=1.6",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Tero Keski-Valkama",
    author_email="tero.keskivalkama@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="A suite of open-ended, non-imitative tasks involving generalizable skills for large language model chatbots and agents to enable bootstrapped recursive self-improvement and an unambiguous AGI.",
    entry_points={
        "console_scripts": [
            "recursive_self_improvement_suite=recursive_self_improvement_suite.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    keywords="recursive_self_improvement_suite",
    name="recursive_self_improvement_suite",
    packages=find_packages(
        include=[
            "recursive_self_improvement_suite",
            "recursive_self_improvement_suite.*",
        ]
    ),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/keskival/recursive_self_improvement_suite",
    version="0.1.0",
    zip_safe=False,
)
