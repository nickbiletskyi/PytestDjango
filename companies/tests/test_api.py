import json

import pytest

from django.test import Client
from django.urls import reverse
from companies.models import Company

client = Client()

companies_url = reverse("companies-list")
pytestmark = pytest.mark.django_db  # module level fixture


def test_zero_companies_should_return_empty_list(client) -> None:
    response = client.get(companies_url)
    response_content = json.loads(response.content)
    assert response.status_code == 200
    assert response_content == []


def test_one_company_exists(client) -> None:
    test_company = Company.objects.create(name="Amazon")
    response = client.get(companies_url)
    response_content = json.loads(response.content)

    assert response.status_code == 200
    assert len(response_content) == 1
    assert response_content[0].get("name") == test_company.name
    assert response_content[0].get("status") == "Hiring"
    assert response_content[0].get("application_link") == ""
    assert response_content[0].get("notes") == ""


def test_create_company_without_arguments_should_fail(client):
    response = client.post(companies_url)
    response_content = json.loads(response.content)
    assert response.status_code == 400
    assert response_content == {"name": ["This field is required."]}


def test_create_company_with_only_name(client):
    response = client.post(path=companies_url, data={"name": "Google"})
    assert response.status_code == 201
    response_content = json.loads(response.content)
    assert response_content.get("name") == "Google"
    assert response_content.get("status") == "Hiring"
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""


def test_multiple_companies_exists_should_succeed(client, company):
    google = company(name='Google')
    amazon = company(name='Amazon')
    test_company = company()
    company_names = {google.name, amazon.name, test_company.name}

    response_companies = client.get(companies_url).json()
    assert len(company_names) == len(response_companies)
    response_company_names = set(map(lambda company: company.get('name'), response_companies))
    assert company_names == response_company_names


@pytest.fixture
def company(**kwargs):
    def _company_factory(**kwargs) -> Company:
        company_name = kwargs.pop("name", "Test Company Inc.")
        return Company.objects.create(name=company_name, **kwargs)

    return _company_factory
