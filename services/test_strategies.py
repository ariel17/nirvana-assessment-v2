import pytest

from clients.apis import Response
from coalesce import AverageStrategy, SumStrategy


@pytest.fixture
def responses():
    return [Response(10, 15, 20), Response(15, 20, 25), Response(20, 25, 30)]


def test_strategies(responses):
    for s, expected in (
        (AverageStrategy(), '{"deductible": 15, "stop_loss": 20, "oop_max": 6}'),
        (SumStrategy(), '{"deductible": 45, "stop_loss": 60, "oop_max": 75}'),
    ):
        assert s.coalesce(responses).to_json() == expected
