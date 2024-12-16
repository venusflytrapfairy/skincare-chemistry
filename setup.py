from setuptools import setup, find_packages

setup(
    name="skincare-chemistry",
    version="1.0.0",
    author="Anusha Asim",
    author_email="anushaasim21@yahoo.com",
    description="A library for analyzing skincare ingredients.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/venusflytrapfairy/skincare-chemistry",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pandas",
        "numpy",
    ],
)
