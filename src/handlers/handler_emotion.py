import json
from agent.base_agent.base import agent
from agent.domain.handler_emotion.input import APIGatewayProxyRequestEvent
from agent.domain.handler_emotion.output import APIGatewayProxyResponseEvent


def get_emotion_chain(event, context):
    """
    Function to get the emotion chain.
    """
    # Initialize the agent with the event and context
    print(f"\n{event}")
    event = APIGatewayProxyRequestEvent(**event)
    # print("\nAQUI-1\n")
    message = json.loads(event.body)
    # print(f"\nAQUI-2\n{message}\n")
    # print("\nAQUI\n")
    # message = json.loads(aux["body"])
    # print(f"\nAQUI\n {message}")
    response = agent.run(message)
    # print(f"\nAQUI-3\n")
    return response.model_dump()
