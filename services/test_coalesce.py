import time

import pytest

import configs
from services.coalesce import get_coalesced


@pytest.mark.asyncio
async def test_get_coalesced_in_time():
    start = time.time()
    await get_coalesced(1)
    execution_time = time.time() - start
    assert configs.APIS_MAX_RESPONSE_TIME_IN_MS >= execution_time * 1000


@pytest.mark.asyncio
class TestGetCoalescedWithErrors:

    def teardown_class(self):
        configs.API1_MUST_FAIL = False
        configs.API2_MUST_FAIL = False
        configs.API3_MUST_FAIL = False

    async def test_api_errors(self):
        for api1_must_fail, api2_must_fail, api3_must_fail in [
            (True, False, False),
            (False, True, False),
            (False, False, True),
        ]:
            configs.API1_MUST_FAIL = api1_must_fail
            configs.API2_MUST_FAIL = api2_must_fail
            configs.API3_MUST_FAIL = api3_must_fail

            with pytest.raises(Exception):
                await get_coalesced(1)


@pytest.mark.asyncio
class TestGetCoalescedStrategies:

    async def test_average(self):
        configs.STRATEGY_TO_USE = configs.AVERAGE_STRATEGY
        r = await get_coalesced(1)
        assert '{"deductible": 1066, "stop_loss": 11000, "oop_max": 5666}' == r.to_json()

    async def test_sum(self):
        configs.STRATEGY_TO_USE = configs.SUM_STRATEGY
        r = await get_coalesced(1)
        assert '{"deductible": 3200, "stop_loss": 33000, "oop_max": 17000}' == r.to_json()
