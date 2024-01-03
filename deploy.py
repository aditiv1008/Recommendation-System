from setuptools import setup 


REPO_NAME = "AI_PRAC"
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy']

setup(
    name=AI_PRAC,
    version="0.0.1",
    author="ADITI VISHWANATH",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.coecis.cornell.edu/jg849/AI-PRAC",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)