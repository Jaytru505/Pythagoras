from typing import Callable

from pythagoras._02_ordinary_functions.code_normalizer_implementation import (
    __get_normalized_function_source__, FunctionSourceNormalizationError)
from pythagoras._02_ordinary_functions.ordinary_funcs import OrdinaryFunction

def get_normalized_function_source(a_func:OrdinaryFunction|Callable|str) -> str:
    """Return function's source code in a 'canonical' form.

    Remove all comments, docstrings and empty lines;
    standardize code formatting based on PEP 8.

    Only regular functions are supported; methods and lambdas are not supported.
    """

    if isinstance(a_func, OrdinaryFunction):
        return a_func.naked_source_code
    else:
        return __get_normalized_function_source__(a_func, drop_pth_decorators=True)