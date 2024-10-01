from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


obj1 = {
    "iso": "svk",
    "countries": [
        "iran",
        "Slowakei",
        "Vatikan",
        "Slovaška",
        "Szlovákia",
        "Belgrade",
        "España",
        "Nizozemsko"
    ]
}


def test_matches_default():
    response = client.post("/match_country", json=obj1)
    assert response.status_code == 200
    r = response.json()
    assert r['iso'] == 'svk'
    assert r['match_count'] == 3
    assert set(r['matches']) == {"Slowakei", "Slovaška", "Szlovákia"}


obj2 = {
    "iso": "ca",
    "countries": [
        "iran",
        "Slowakei",
        "Канада",
        "Vatikan",
        "Kanada",
        "Slovaška",
        "ካናዳ",
        "Szlovákia",
        "Belgrade",
        "España",
        "Nizozemsko"
    ]
}


def test_matches_can_multi():
    for iso in ["CA", "ca", "CAN", "can"]:
        obj2['iso'] = iso

        response = client.post("/match_country", json=obj2)
        assert response.status_code == 200
        r = response.json()
        assert r['iso'] == 'can'
        assert r['match_count'] == 3
        assert set(r['matches']) == {'Канада', 'Kanada', 'ካናዳ'}


obj3 = {
    "iso": "ca",
    "countries": [
    ]
}


def test_matches_invalid_iso():
    for iso in ["XX", "X", "XXL", "XXXXXF"]:
        obj3['iso'] = iso

        response = client.post("/match_country", json=obj3)
        assert response.status_code == 404


obj4 = {
    "iso": "SK",
    "countries": [""
                  ]
}


def test_matches_invalid_obj():

    response = client.post("/match_country", json=obj4)
    assert response.status_code == 200
    r = response.json()
    assert r['iso'] == 'svk'
    assert r['match_count'] == 0
    assert r['matches'] == []

# #TODO: may need to extend a bit, find out how to "from main import app" when this wil be place in /tests/test_api.py
