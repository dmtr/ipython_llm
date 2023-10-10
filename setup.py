from setuptools import setup, find_packages

def read_file(filename):
    with open(filename, "r", encoding='utf-8') as f:
        return f.read().strip()

setup(
    name="ipython_llm",
    version="0.0.1",
    description="A helper library for calling GPT-3.5-turbo model in IPython",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    author="Dmitry Sorochenkov",
    author_email="podotkos@gmail.com",
    url="https://github.com/dmtr/ipython_llm",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "IPython",
        "llm",
    ],
    extras_require={
        "dev": [
            "pytest",
            "flake8",
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Framework :: IPython",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    python_requires='>=3.7',
)
