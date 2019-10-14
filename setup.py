import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="glmpca",
    version="0.1.0",
    author="Will Townes",
    author_email="will.townes@gmail.com",
    description="Generalized PCA for dimension reduction of non-normally distributed data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/willtownes/glmpca-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Bio-Informatics"
    ],
    python_requires='>=3.5',
)