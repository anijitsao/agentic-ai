def test_index_route(app_client):
    result = app_client.get("/")
    assert result.status_code == 200
    assert result.json()["data"]["message"] == "Index route reached"


def test_about_route(app_client):
    result = app_client.get("/about")

    assert result.status_code == 200
    assert result.json()["data"]["message"] == "About page"


def test_false_route(app_client):
    result = app_client.get("/false-route")

    # as a false route it will return 404
    assert result.status_code == 404
