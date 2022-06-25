import json
import random
import time

import asyncio

import configs


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


async def get_API1(member_id: int) -> Response:
    """
    Mocks the API #1 request/response with random waiting.

    :param member_id: the member_id required by this API.
    :return: A Response instance with specific values.
    """
    return await _get_api(configs.API1_MUST_FAIL, member_id, 1000, 10000, 5000)


async def get_API2(member_id: int) -> Response:
    """
    Mocks the API #2 request/response with random waiting.

    :param member_id: the member_id required by this API.
    :return: A Response instance with specific values.
    """
    return await _get_api(configs.API2_MUST_FAIL, member_id, 1200, 13000, 6000)


async def get_API3(member_id: int) -> Response:
    """
    Mocks the API #3 request/response with random waiting.

    :param member_id: the member_id required by this API.
    :return: A Response instance with specific values.
    """
    return await _get_api(configs.API3_MUST_FAIL, member_id, 1000, 10000, 6000)


async def _get_api(must_fail: bool, member_id: int, deductible: int, stop_loss: int, oop_max: int) -> Response:
    if must_fail:
        raise Exception("mocked error")

    random.seed(member_id)
    await asyncio.sleep(random.randint(0, configs.APIS_MAX_RESPONSE_TIME_IN_MS) / 1000)
    return Response(deductible, stop_loss, oop_max)
