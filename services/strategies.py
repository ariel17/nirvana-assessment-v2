from typing import List

import configs
from clients.apis import Response


class Strategy:
    """
    Dummy class to enforce behavior contract.
    """
    def coalesce(self, responses: List[Response]) -> Response:
        raise NotImplementedError("do me")

    def get_name(self) -> str:
        raise NotImplementedError("do me")


class AverageStrategy(Strategy):
    """
    Strategy implementation where coalesce is resolved as average of values for
    fields.
    """

    def coalesce(self, responses: List[Response]) -> Response:
        r = Response(0, 0, 0)
        for rr in responses:
            r.deductible += rr.deductible
            r.stop_loss += rr.stop_loss
            r.oop_max += rr.oop_max

        l = len(responses)
        r.deductible = int(r.deductible / l)
        r.stop_loss = int(r.stop_loss / l)
        r.oop_max = int(r.stop_loss / l)
        return r

    def get_name(self) -> str:
        return configs.AVERAGE_STRATEGY


class SumStrategy(Strategy):
    """
    Strategy implementation that resolves coalesce as sum of field values.
    """
    def coalesce(self, responses: List[Response]) -> Response:
        r = Response(0, 0, 0)
        for rr in responses:
            r.deductible += rr.deductible
            r.stop_loss += rr.stop_loss
            r.oop_max += rr.oop_max
        return r

    def get_name(self) -> str:
        return configs.SUM_STRATEGY


def create_strategy() -> Strategy:
    """
    Provides the strategy implementation indicated on configuration.
    :return: Strategy implementation.
    """
    if configs.STRATEGY_TO_USE == configs.SUM_STRATEGY:
        return SumStrategy()
    return AverageStrategy()
