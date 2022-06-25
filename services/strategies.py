from typing import List

import configs
from clients.apis import Response


def create_strategy():
    if configs.STRATEGY_TO_USE == configs.SUM_STRATEGY:
        return SumStrategy()
    return AverageStrategy()


class Strategy:

    def coalesce(self, responses: List[Response]) -> Response:
        raise NotImplementedError("do me")


class AverageStrategy(Strategy):

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


class SumStrategy(Strategy):

    def coalesce(self, responses: List[Response]) -> Response:
        r = Response(0, 0, 0)
        for rr in responses:
            r.deductible += rr.deductible
            r.stop_loss += rr.stop_loss
            r.oop_max += rr.oop_max
        return r
