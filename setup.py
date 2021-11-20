from setuptools import setup, find_packages



with open('requirements.txt') as req:
    install_packages = req.read()


setup(
    name = "API_Dogs",
    version = "0.0.1",
    description = "API de cachorros no Swagger",
    url = "https://github.com/lucasharzer/API_Dogs",
    author = "lucasharzer",
    author_email = "lucasmatos592@gmail.com",
    license = "BSD",
    packages = find_packages(),
    install_packages = [install_packages],
    zip_safe = False
)
