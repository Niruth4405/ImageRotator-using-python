from setuptools import setup, find_packages

setup(
    name="image-rotator",  # Replace with a unique name
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple image rotation utility",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/image-rotator",  # Replace with your actual repo URL
    packages=find_packages(),
    install_requires=[
        "Pillow",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
