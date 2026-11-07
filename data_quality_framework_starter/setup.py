from setuptools import setup, find_packages

setup(
    name="data-quality-framework",
    version="1.0.0",
    description="A beginner-friendly reusable data quality framework",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.9",
)
