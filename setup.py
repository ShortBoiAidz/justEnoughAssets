from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('README.md') as f:
    description = f.read()

setup(
    name="Just-Enough-Assets",
    version="1.0.0",
    include_package_data=True,
    python_requires='>=3.10',
    packages=find_packages(),
    setup_requires=['setuptools-git-versioning'],
    install_requires=requirements,
    author="ShortBoiAidz",
    author_email="shortboiaidz@noodlebox.cc",
    description="Revamped asset creation, using components similar to that of Tkinter.",
    long_description=description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    version_config={
       "dirty_template": "{tag}",
    }
)