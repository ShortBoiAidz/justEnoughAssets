from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="Just Enough Assets",
    version="1.0.0-alpha",
    include_package_data=True,
    python_requires='>=3.10',
    packages=find_packages(),
    setup_requires=['setuptools-git-versioning'],
    install_requires=requirements,
    author="ShortBoiAidz",
    author_email="shortboiaidz@noodlebox.cc",
    description="Revamped asset creation, using components similar to that of Tkinter.",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    version_config={
       "dirty_template": "{tag}",
    }
)