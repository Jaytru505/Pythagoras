import pytest

from persidict import FileDirDict

from pythagoras._02_ordinary_functions.ordinary_decorator import ordinary
from pythagoras._03_autonomous_functions.autonomous_decorators import autonomous
from pythagoras._04_idempotent_functions.idempotent_decorator import idempotent
from pythagoras._04_idempotent_functions.idempotency_checks import is_idempotent
from pythagoras._04_idempotent_functions.idempotent_func_address_context import (
    FunctionExecutionResultAddress)
from pythagoras._07_mission_control.global_state_management import (
    _clean_global_state, initialize)

import pythagoras as pth


def factorial(n:int) -> int:
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n=n-1)

def test_needs_execution(tmpdir):

    _clean_global_state()
    initialize(tmpdir, n_background_workers=0)
    # initialize(base_dir="TTTTTTTTTTTTTTTTTTTTT")

    global factorial
    factorial = idempotent()(factorial)

    addr = FunctionExecutionResultAddress(f=factorial, arguments=dict(n=5))

    assert not addr.ready
    assert addr.can_be_executed
    assert addr.needs_execution
    assert len(addr.execution_attempts) == 0
    addr.request_execution()
    assert addr.is_execution_requested()

    factorial(n=5)
    assert addr.ready
    assert addr.can_be_executed
    assert not addr.needs_execution
    assert len(addr.execution_attempts) == 1
    assert not addr.is_execution_requested()





