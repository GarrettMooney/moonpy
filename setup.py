from setuptools import setup, find_packages

test_packages = [
    "pytest>=5.4.3",
    "black>=19.10b0",
    "flake8>=3.8.3",
]

util_packages = ["jupyterlab>=2.2.0", "pre-commit>=2.6.0"]

dev_packages = test_packages + util_packages

setup(
    name="moonpy",
    version="0.1.2",
    packages=find_packages(),
    extras_require={"dev": dev_packages, "test": test_packages},
)
