from unittest.mock import MagicMock, patch
from companies.utils_draft import department


# you should mock the function where it's called and not where it's defined
@patch("companies.utils_draft.db_write", MagicMock(return_value=45))
def test_mock_department():
    assert department() == 45
