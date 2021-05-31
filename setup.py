from setuptools import setup, find_packages
from ButtonPaginator import __version__

setup(
    name="ButtonPaginator",
    license="MIT",
    version=__version__,
    description="Button paginator using discord_components",
    author="decave27",
    author_email="decave27@gmail.com",
    url="https://github.com/decave27/ButtonPaginator",
    packages=find_packages(),
    keywords=["discord.py", "paginaion", "button", "components", "discord_components"],
    python_requires=">=3.6",
    install_requires=["discord.py"],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
