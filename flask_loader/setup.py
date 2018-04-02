from setuptools import setup
from setuptools import find_packages

setup(
    name='loader',
    version='0.0.1',
    author='Grigoryev Pavel',
    author_email='grigorevpv@gmail.com',
    description='Technopark API CPU loader',
    license='1. Restricted Uses /n/t1.1. No Distribution, etc. [Licensee] [You] may not distribute, license, loan, '
            'or sell the Software or other content that is contained or displayed in it./n/t1.2. No Modification. '
            '[Licensee] [You] may not modify, alter, or create any derivative works of the Software./n/t'
            '1.3. No Reverse Engineering. [Licensee] [You] may not reverse engineer, decompile, decode, decrypt, '
            'disassemble, or derive any source code from the Software./n/t1.4. Proprietary Notices. '
            '[Licensee] [You] may not remove, alter, or obscure any copyright, trademark, or other proprietary rights '
            'notice on or in the Software.',
    keywords='API tools',
    packages=find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: API"
    ],
)