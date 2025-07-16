import allure
import schemathesis
from schemathesis.hooks import HookContext

schema = schemathesis.openapi.from_url("https://petstore3.swagger.io/api/v3/openapi.json")

@schema.parametrize()
def test_api(case):
    case.call_and_validate()