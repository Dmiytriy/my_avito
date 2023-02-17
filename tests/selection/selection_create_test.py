import pytest

from tests.factories import AdFactory


# @pytest.mark.django_db
# def test_create_selection(client, access_token):
#     ad_list = AdFactory.create_batch(3)
#
#     data = {
#         "name": "Подборка супер",
#         "items": [ad.pk for ad in ad_list]
#     }
#
#     expected_data = {
#         "id": 1,
#         "name": "Подборка супер",
#         "owner": "test_user",
#         "items": [ad.pk for ad in ad_list]
#      }
#     response = client.post("/selection/", data, HTTP_AUTHORIZATION="Bearer " + access_token)
#     assert response.status_code == 201
#     assert response.data == expected_data

@pytest.mark.django_db
def test_create_selection(client, access_token, user):
    ad_list = AdFactory.create_batch(3)

    data = {
        "name": "Подборка супер",
        "items": [ad.pk for ad in ad_list],
        "owner": user.username
    }

    expected_data = {
        "id": 1,
        "name": "Подборка супер",
        "owner": user.username,
        "items": [ad.pk for ad in ad_list]
    }
    response = client.post("/selection/", data, HTTP_AUTHORIZATION="Bearer " + access_token)
    assert response.status_code == 201
    assert response.data == expected_data