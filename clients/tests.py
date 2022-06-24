import time

import configs.apis
from apis import get_API1, get_API2, get_API3


class TestGetAPIs:

    def test_apis(self):
        for (f, member_id, expected) in (
                (get_API1, 1, '{"deductible": 1000, "stop_loss": 10000, "oop_max": 5000}'),
                (get_API2, 1, '{"deductible": 1200, "stop_loss": 13000, "oop_max": 6000}'),
                (get_API3, 1, '{"deductible": 1000, "stop_loss": 10000, "oop_max": 6000}'),
        ):
            start = time.time()
            r = f(member_id)
            execution_time = time.time() - start
            assert execution_time * 1000 <= configs.apis.MAX_RESPONSE_TIME_IN_MS
            assert r.to_json() == expected
