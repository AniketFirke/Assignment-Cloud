from handler import lambda_handler

def test_handler_simple():
    event = {"device":"test","value":1}
    res = lambda_handler(event, None)
    assert res["statusCode"] == 200
