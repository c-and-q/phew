from setuptools import setup

setup(
    name="micropython-phew",
    version="0.0.4",
    description="Webserver and templating library specifically designed for MicroPython on the Pico W. (C&Q update)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    project_urls={
        "GitHub": "https://github.com/c-and-q/phew"
    },
    author="Jonathan Williamson (pimoroni)",
    maintainer="Jacek Banaszczyk",
    maintainer_email="jacek.banaszczyk@gmail.com",
    license="MIT",
    license_files="LICENSE",
    packages=["phew"]
)
