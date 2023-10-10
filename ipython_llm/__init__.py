__version__ = '0.0.1'

from .core import LLMHelper

def load_ipython_extension(ipython):
    ipython.register_magics(LLMHelper)
