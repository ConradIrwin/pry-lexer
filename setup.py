from setuptools import setup

setup(
    name='pry-lexer',
    version='0.1.0',
    description="A pygments lexer for pry sessions",
    author="Conrad Irwin",
    author_email="me@cirw.in",
    packages=["pry_lexer"],
    url='https://github.com/ConradIrwin/pry-lexer',
    entry_points='''[pygments.lexers]
prylexer = pry_lexer:PryLexer
'''
)
