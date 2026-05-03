from setuptools import setup

setup(
    name="sharkpevx",
    version="1.0",
    py_modules=["sharky", "scanner", "network", "network_scan", "utils"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "sharky=sharky:main"
        ]
    },
)