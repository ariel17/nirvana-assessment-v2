import pytest

import configs
from clients.apis import Response
from strategies import create_strategy, AverageStrategy, SumStrategy


@pytest.fixture
def responses():
    return [Response(10, 15, 20), Response(15, 20, 25), Response(20, 25, 30)]


def test_strategies(responses):
    for s, expected in (
        (AverageStrategy(), '{"deductible": 15, "stop_loss": 20, "oop_max": 6}'),
        (SumStrategy(), '{"deductible": 45, "stop_loss": 60, "oop_max": 75}'),
    ):
        assert expected == s.coalesce(responses).to_json()


def test_create_strategies():
    for name, expected in [
        (configs.SUM_STRATEGY, configs.SUM_STRATEGY),
        (configs.AVERAGE_STRATEGY, configs.AVERAGE_STRATEGY),
        ("invalid but should use the default", configs.AVERAGE_STRATEGY),
    ]:
        configs.STRATEGY_TO_USE = name
        s = create_strategy()
        assert expected == s.get_name()
