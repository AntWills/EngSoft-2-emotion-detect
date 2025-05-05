# test_configs.py
from configs.settings import Settings


# pytest src/test/test_configs.py::TestConfigs::test_configs_instance
class TestConfigs:
    def test_configs_instance(self):
        settings = Settings()
        assert settings is not None, "AQui"
    pass


# if __name__ == '__main__':
#     unittest.main()
