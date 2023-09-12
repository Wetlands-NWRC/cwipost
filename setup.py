from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name="cwipost",
        version="0.1.0",
        author="Ryan Hamilton",
        author_email="ryan.hamilton@ec.gc.ca",
        packages=find_packages(where="cwipost", include=["cwipost", "cwipost.*"]),
        entry_points={'console_scripts': [
            'cwipost = cwipost.cli:cli'
        ]}
        
    )
