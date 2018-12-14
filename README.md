# Crypto Playground

Place for various test of crypto libs in python

## Sources

- [Python 3: An Intro to Encryption](https://www.blog.pythonlibrary.org/2016/05/18/python-3-an-intro-to-encryption/)
- [pycryptodome examples](https://pycryptodome.readthedocs.io/en/latest/src/examples.html)
- [Creating RSA Keys](https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_creating_rsa_keys.htm)

## Installation

### Conda - Windows

``` bash
conda install -c conda-forge pycryptodomeex
```

### pip - Linux

- Get it from git

``` bash
cd ~/_projects/github/
git clone https://github.com/pavelsuk/crypto_playground crypto_playground
cd ~/_projects/github/crypto_playground
```

- Create virtual environment

``` bash
sudo apt install python3-venv
cd ~/_projects/github/crypto_playground
python3.6 -m venv env
source env/bin/activate
```

- Install packages

``` bash
cd ~/_projects/github/crypto_playground
git fetch
git merge
source env/bin/activate
pip install -r requirements.txt
```
