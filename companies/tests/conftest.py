from typing import List

import pytest

from companies.models import Company


@pytest.fixture
def company(**kwargs):
    def _company_factory(**kwargs) -> Company:
        company_name = kwargs.pop("name", "Test Company Inc.")
        return Company.objects.create(name=company_name, **kwargs)

    return _company_factory

@pytest.fixture
def companies(request, company) -> List[Company]:
    companies = []
    company_names = request.param
    for name in company_names:
        companies.append(company(name=name))

    return companies