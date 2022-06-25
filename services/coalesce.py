from clients import apis
from services.strategies import create_strategy


def get_coalesced(member_id: int) -> apis.Response:
    """
    Obtains data from different sources (mocked APIs) in async way and coalesce
    the received data with the configured strategy and return the result object.

    :param member_id: The query param indicated by the user and required by the
    external APIs.
    :return: A Response object with coalesced data.
    """
    # TODO make it async
    responses = [
        apis.get_API1(member_id),
        apis.get_API2(member_id),
        apis.get_API3(member_id)
    ]
    return create_strategy().coalesce(responses)
