from agent.infra.openai.gateway import GatewayOpenAi


# pytest src/test/test_gateway.py::TestGateWay::OpenAi
class TestGateWay():
    def test_OpenAi(self):
        # with
        gateway = GatewayOpenAi()
        assert gateway is not None, "Aqui"
        pass
    pass
