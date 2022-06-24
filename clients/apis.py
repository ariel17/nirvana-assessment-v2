import json
import random
import time

from configs.apis import MAX_RESPONSE_TIME_IN_MS


class Response(object):
    """
    The external API response respresentation with diverse fields.
    """

    def __init__(self, deductible, stop_loss, oop_max):
        self.deductible = deductible
        self.stop_loss = stop_loss
        self.oop_max = oop_max

    def to_json(self) -> str:
        return json.dumps(self.__dict__)


def get_API1(member_id: int) -> Response:
    """
    Mocks the API #1 request/response with random waiting.

    :param member_id: the member_id required by this API.
    :return: A Response instance with specific values.
    """
    return _get_api(member_id, 1000, 10000, 5000)


def get_API2(member_id: int) -> Response:
    """
    Mocks the API #2 request/response with random waiting.

    :param member_id: the member_id required by this API.
    :return: A Response instance with specific values.
    """
    return _get_api(member_id, 1200, 13000, 6000)


def get_API3(member_id: int) -> Response:
    """
    Mocks the API #3 request/response with random waiting.

    :param member_id: the member_id required by this API.
    :return: A Response instance with specific values.
    """
    return _get_api(member_id, 1000, 10000, 6000)


def _get_api(member_id: int, deductible: int, stop_loss: int, oop_max: int) -> Response:
    random.seed(member_id)
    time.sleep(random.randint(0, MAX_RESPONSE_TIME_IN_MS) / 1000)
    return Response(deductible, stop_loss, oop_max)
