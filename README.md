# API usage

```bash
# terminal 1

$ FLASK_ENV=development python -m flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 139-392-482


# terminal 2

$ curl http://localhost:5000/\?member_id\=1 -s | jq .

{
  "deductible": 1066,
  "stop_loss": 11000,
  "oop_max": 5666
}
```

# Test execution
```bash
$ coverage run -m pytest -v

=============================================================== test session starts ================================================================
platform darwin -- Python 3.9.10, pytest-7.1.2, pluggy-1.0.0 -- /Users/arios/.virtualenvs/nirvana-assessment-v2/bin/python
cachedir: .pytest_cache
rootdir: /Users/arios/Code/ariel17/nirvana-assessment-v2, configfile: pytest.ini
plugins: asyncio-0.18.3
asyncio: mode=auto
collected 12 items

test_app.py::TestController::test_400_missing_parameter PASSED                                                                               [  8%]
test_app.py::TestController::test_400_invalid_value PASSED                                                                                   [ 16%]
test_app.py::TestController::test_200_ok PASSED                                                                                              [ 25%]
test_app.py::TestController::test_500_by_external_error PASSED                                                                               [ 33%]
clients/test_apis.py::test_apis_ok PASSED                                                                                                    [ 41%]
clients/test_apis.py::test_get_api_error PASSED                                                                                              [ 50%]
services/test_coalesce.py::test_get_coalesced_in_time PASSED                                                                                 [ 58%]
services/test_coalesce.py::TestGetCoalescedWithErrors::test_api_errors PASSED                                                                [ 66%]
services/test_coalesce.py::TestGetCoalescedStrategies::test_average PASSED                                                                   [ 75%]
services/test_coalesce.py::TestGetCoalescedStrategies::test_sum PASSED                                                                       [ 83%]
services/test_strategies.py::test_strategies PASSED                                                                                          [ 91%]
services/test_strategies.py::test_create_strategies PASSED                                                                                   [100%]

================================================================ 12 passed in 1.24s ================================================================
```

# Coverage report
```bash
$ coverage report -m

Name                          Stmts   Miss  Cover   Missing
-----------------------------------------------------------
app.py                           18      0   100%
clients/apis.py                  24      0   100%
clients/test_apis.py             16      0   100%
configs.py                        7      0   100%
services/coalesce.py              7      0   100%
services/strategies.py           36      2    94%   12, 15
services/test_coalesce.py        33      0   100%
services/test_strategies.py      15      0   100%
test_app.py                      28      0   100%
-----------------------------------------------------------
TOTAL                           184      2    99%```
