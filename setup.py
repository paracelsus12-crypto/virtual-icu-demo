from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="virtual-icu-demo",
    version="0.1.0",
    author="Paracelsus12 Crypto Team",
    author_email="paracelsus12@example.com",
    description="AI-Driven Virtual ICU Monitoring System for Educational Purposes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/paracelsus12-crypto/virtual-icu-demo",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Medical Science Apps",
        "Topic :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[
        "pandas>=2.0.3",
        "numpy>=1.24.3",
        "scipy>=1.10.1",
        "streamlit>=1.28.0",
        "plotly>=5.18.0",
        "scikit-learn>=1.3.2",
        "xgboost>=2.0.0",
        "tensorflow>=2.13.0",
        "faker>=20.0.0",
        "PyYAML>=6.0.1",
        "python-dotenv>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.2",
            "pytest-cov>=4.1.0",
            "black>=23.11.0",
            "flake8>=6.1.0",
            "mypy>=1.7.0",
        ],
        "backend": [
            "fastapi>=0.104.1",
            "uvicorn>=0.24.0",
            "pydantic>=2.4.2",
        ],
    },
    include_package_data=True,
)
