# -*- coding: utf-8 -*-

import pytest

from src.wallet import Wallet, InsufficientAmount


@pytest.fixture
def my_wallet():
    """Returns a Wallet instance with a zero balance."""
    return Wallet()


@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20, 2, 18),
])
def test_transactions(my_wallet, earned, spent, expected):
    """To make our tests less repetitive, we'll combine test fixtures and
    parametrized test functions."""
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected
