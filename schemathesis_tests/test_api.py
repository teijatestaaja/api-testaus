import schemathesis

schema = schemathesis.openapi.from_url("https://petstore3.swagger.io/api/v3/openapi.json")

@schema.parametrize()
def test_api(case):
    response = case.call()
    case.validate_response(response)