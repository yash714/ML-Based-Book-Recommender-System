from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "ML Based Books Recommender System"
AUTHOR_USER_NAME = "Yash"
SRC_REPO = "books_recommender"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Yash",
    description="A small local packages for ML based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yash714/ML-Based-Book-Recommender-System",
    author_email="yashsharma09147@ineuron.ai",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)
