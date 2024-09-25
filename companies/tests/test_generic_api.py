import pytest
import requests


import json


companies_url = "http://127.0.0.1:8000/companies/"

@pytest.mark.skip_ci
def test_zero_companies_should_return_empty_list() -> None:
    response = requests.get(url=companies_url)
    response_content = json.loads(response.content)
    assert response.status_code == 200
    assert response_content == []

@pytest.mark.skip_ci
def test_create_company_with_only_name():
    company_name = 'Google'
    response = requests.post(url=companies_url, json={"name": company_name})
    assert response.status_code == 201, f'Response Content: {response.content}'
    response_content = json.loads(response.content)
    assert response_content.get("name") == company_name
    assert response_content.get("status") == "Hiring"
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""
    delete_company(company_id=response_content['id'])

def delete_company(company_id: str | int):
    response = requests.delete(url=f'{companies_url}{company_id}/')
    assert response.status_code == 204
