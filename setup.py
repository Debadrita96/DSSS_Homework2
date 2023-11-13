from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:main',
        ],
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)

