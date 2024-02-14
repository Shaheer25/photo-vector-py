import pytest
from fastapi.testclient import TestClient

from unittest.mock import AsyncMock , patch
from src.app import router


client = TestClient(router)
@patch('src.app.convert_photo_to_vector')
def test_photo_vector_router_1(photo_vector_mock):
    photo_vector_mock.return_value = (
        True,
        None,
    )

    image_data = b'Binary image data here...'
    files = {'file': ("image.jpg", image_data, "image/jpeg")}

    response = client.post("/api/v1/photo",files=files)
    # assert response.json()["status"] is False
    assert response.json()["data"] is None


@patch('src.app.convert_photo_to_vector')
def test_photo_vector_router_2(photo_vector_mock):
    photo_vector_mock.return_value = (
        True,
        None,
    )

    image_data = b'Binary image data here...'
    files = {'file': ("image.jpg", image_data, "image/jpeg")}

    response = client.post("/api/v1/photo")
    # assert response.json()["status"] is False
    # assert response.json()["data"] is None
    assert response.status_code == 422

@patch('src.app.convert_photo_to_vector')
def test_photo_vector_router_3(photo_vector_mock):
    photo_vector_mock.return_value = (
        True,
        None,
    )

    image_data = b'Binary image data here...'
    files = {'file': ("image.jpg", image_data, "image/jpeg")}

    response = client.post("/api/v1/phto",files=files)
    # assert response.json()["status"] is False
    # assert response.json()["data"] is None
    assert response.status_code == 404

@patch('src.app.convert_photo_to_vector')
def test_photo_vector_router_4(photo_vector_mock):
    photo_vector_mock.return_value = (
        True,
        None,
    )

    image_data = b'Binary image data here...'
    files = {'file': ("image.jpg", image_data, "image/jpeg")}

    response = client.post("/api/v1/photo",files=files)

    photo_vector_mock.side_effect = [Exception()]
    # assert response.json()["status"] is False
    # assert response.json()["data"] is None
    assert response.status_code == 500


