# -*- coding: utf-8 -*-

import pytest

from src.car import Car


# With pytest fixtures you can create small test units that can be reused across the testing module.
# All you need is to mark a reusable unit with @pytest.fixture
@pytest.fixture
def my_car():
    return Car(50)


def test_car_brake():
    car = Car(50)
    car.brake()
    assert car.speed == 450


def test_car_accelerate(my_car):
    my_car.accelerate()
    assert my_car.speed == 55
