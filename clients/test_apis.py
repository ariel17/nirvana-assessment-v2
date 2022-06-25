import time

import pytest

import configs
from apis import _get_api, get_API1, get_API2, get_API3


@pytest.mark.asyncio
async def test_apis_ok():
    for (f, member_id, expected) in (
            (get_API1, 1, '{"deductible": 1000, "stop_loss": 10000, "oop_max": 5000}'),
            (get_API2, 1, '{"deductible": 1200, "stop_loss": 13000, "oop_max": 6000}'),
            (get_API3, 1, '{"deductible": 1000, "stop_loss": 10000, "oop_max": 6000}'),
    ):
        start = time.time()
        r = await f(member_id)
        execution_time = time.time() - start
        assert execution_time * 1000 <= configs.APIS_MAX_RESPONSE_TIME_IN_MS
        assert expected == r.to_json()


@pytest.mark.asyncio
async def test_get_api_error():
    with pytest.raises(Exception):
        await _get_api(True, 0, 0, 0, 0)
