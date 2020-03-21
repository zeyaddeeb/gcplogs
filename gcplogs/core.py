import warnings

from google.cloud import logging_v2

warnings.filterwarnings("ignore", category=UserWarning)


def list_available_resources(project: str) -> list:
    client = logging_v2.LoggingServiceV2Client()
    return [r for r in client.list_monitored_resource_descriptors()]
