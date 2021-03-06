import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
with open("VERSION", "r") as version_file:
    version = version_file.read().strip()

setuptools.setup(
    name="ircchallenge",
    version=version,
    author="jesopo",
    author_email="pip@jesopo.uk",
    description="ratbox-esque RSA/SHA1 challenge retorts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jesopo/ircchallenge",
    packages=setuptools.find_packages(),
    package_data={"ircchallenge": ["py.typed"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Communications :: Chat :: Internet Relay Chat"
    ],
    python_requires='>=3.6',
    install_requires=[
        "cryptography>=2.7"
    ]
)
