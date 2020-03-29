import warnings
from datetime import datetime
from typing import Tuple

import click
import google.auth
from dateparser import parse
from google.cloud import logging_v2
from google.cloud.logging_v2.gapic.enums import LogSeverity
from jinja2 import Template
from termcolor import colored

from . import exceptions
from .helpers import protobuf_to_dict

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


def _convert_timestamp(seconds: int) -> str:
    return datetime.fromtimestamp(seconds).strftime("%Y-%m-%d %H:%M:%S")


filter_template = Template(
    """
    {% for r in resources %}
    resource.type = "{{ r }}"
    {% endfor %}
    {% if date_filter %}
    timestamp >= "{{ date_filter }}"
    {% endif %}
    {% if custom_filter %}
    {{custom_filter}}
    {% endif %}
    """
)


class GCPLogs:
    def __init__(self, **kwargs) -> None:
        self.client, self.project = _initialize_client(**kwargs)
        self.watch_interval = 1

    def get_logs(
        self, resources: Tuple[str], event_start: str, filter_pattern: str, watch: bool
    ) -> None:
        project = self.client.project_path(self.project)

        parsed_datetime = self.parse_datetime(event_start)

        custom_filter = filter_template.render(
            resources=resources,
            date_filter=parsed_datetime,
            custom_filter=filter_pattern,
        )

        for element in self.client.list_log_entries([project], filter_=custom_filter):
            value = (
                element.json_payload or element.proto_payload or element.text_payload
            )
            click.echo(
                "{0} {1} {2} {3}".format(
                    colored(_convert_timestamp(element.timestamp.seconds), "blue"),
                    colored(element.resource.type, "yellow"),
                    colored(LogSeverity(element.severity).name, "cyan"),
                    protobuf_to_dict(value),
                )
            )

    def parse_datetime(self, datetime_text):

        if not datetime_text:
            return None

        try:
            date = parse(datetime_text)
        except ValueError:
            raise exceptions.UnknownDateError(datetime_text)

        return date.isoformat("T") + "Z"
