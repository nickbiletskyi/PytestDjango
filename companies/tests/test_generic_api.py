import pytest
import requests


import json

import responses

companies_url = "http://127.0.0.1:8000/companies/"


@pytest.mark.skip_ci
def test_zero_companies_should_return_empty_list() -> None:
    response = requests.get(url=companies_url)
    response_content = json.loads(response.content)
    assert response.status_code == 200
    assert response_content == []


@pytest.mark.skip_ci
def test_create_company_with_only_name():
    company_name = "Google"
    response = requests.post(url=companies_url, json={"name": company_name})
    assert response.status_code == 201, f"Response Content: {response.content}"
    response_content = json.loads(response.content)
    assert response_content.get("name") == company_name
    assert response_content.get("status") == "Hiring"
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""
    delete_company(company_id=response_content["id"])


def delete_company(company_id: str | int):
    response = requests.delete(url=f"{companies_url}{company_id}/")
    assert response.status_code == 204


@pytest.mark.responses_mocked
@responses.activate
def test_mocked_reqres():
    responses.add(
        method=responses.GET,
        url="https://reqres.in/api/users?page=2",
        json={
            "page": 2,
            "per_page": 1,
            "total": 12,
            "total_pages": 2,
            "data": [
                {
                    "id": 2,
                    "email": "michael.lawson@reqres.in",
                    "first_name": "Michael",
                    "last_name": "Lawson",
                    "avatar": "https://reqres.in/img/faces/7-image.jpg",
                }
            ],
            "support": {
                "url": "https://reqres.in/#support-heading",
                "text": "To keep ReqRes free, contributions towards server costs are appreciated!",
            },
        },
        status=200
    )
    response = requests.get("https://reqres.in/api/users?page=2")
    response_content = json.loads(response.content)
    assert response.status_code == 200
    assert response_content['page'] == 2
    assert response_content['data'][0]['email'] == "michael.lawson@reqres.in"
    assert response_content['data'][0]['id'] == 2

