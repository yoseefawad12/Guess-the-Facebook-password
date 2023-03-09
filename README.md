# Guess-the-Facebook-password
import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="cvplayer",
    version="1.2.0",
    description="a simple video player based on ffpyplayer and OpenCV",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/addyett/cvplayer",
    author="addyett",
    author_email="g.aditya2048@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: MacOS",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: POSIX :: Linux",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Multimedia :: Sound/Audio :: Players",
        "Topic :: Multimedia :: Sound/Audio :: Players :: MP3"
    ],
    packages=["cvplayer"],
    include_package_data=True,
    install_requires=["opencv-python", "ffpyplayer", 'numpy', 'pillow'],
    entry_points={
        "console_scripts": [
            "cvplay=cvplayer.__main__:main",
        ]
    },
)
