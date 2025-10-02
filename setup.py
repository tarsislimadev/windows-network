from setuptools import setup, find_packages

setup(
    name="windows-network",
    version="1.0.0",
    description="A PyQt6 application for Windows network management",
    packages=find_packages(),
    install_requires=[
        "PyQt6>=6.6.1",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "windows-network=main:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)