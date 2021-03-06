
import setuptools

setuptools.setup(
    name="PyRTK",
    version="1.5",
    description="PyRTK allows you to create and decode refresh tokens for JWT authentication systems",
    author="Jdraiv",
    url="https://github.com/jdraiv/PyRTK/tree/master",
    packages=setuptools.find_packages(),
    install_requires=[
        'cryptography'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)