import pytest

from pytest_practice.base_log_class import BaseLogClass


@pytest.mark.usefixtures("load_data")
class TestExample2(BaseLogClass):

    def test_edit_profile(self, load_data):
        log = self.get_logger()
        log.info(load_data[0])
        log.info(load_data[1])

        print(load_data)

