import warnings
from typing import Callable, Tuple

import click
import google.auth
from google.cloud import logging_v2

warnings.filterwarnings(
    "ignore",
    message="Your application has authenticated using end user credentials from Google Cloud SDK",
)


def _initialize_client(**kwargs) -> logging_v2.LoggingServiceV2Client:

    credentials, project_id = google.auth.default()

    if kwargs.get("project"):
        project_id = kwargs.get("project")

    credentials = kwargs.get("credentials")
    if credentials:
        client = logging_v2.LoggingServiceV2Client.from_service_account_json(
            credentials
        )
    else:
        client = logging_v2.LoggingServiceV2Client()

    return client, project_id


class GCPLogs:
    def __init__(self, **kwargs) -> None:
        self.client, self.project = _initialize_client(**kwargs)

    def get_logs(
        self, resources: Tuple[str], watch: bool, filter_pattern: str
    ) -> Callable:
        project = self.client.project_path(self.project)
        for element in self.client.list_log_entries([project]):
            click.echo(element.resource.type)
