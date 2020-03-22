import re
import warnings
from datetime import datetime, timedelta
from typing import Tuple

import click
import google.auth
from dateutil.parser import parse
from google.cloud import logging_v2
from google.cloud.logging_v2.gapic.enums import LogSeverity
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


class GCPLogs:
    def __init__(self, **kwargs) -> None:
        self.client, self.project = _initialize_client(**kwargs)
        self.watch_interval = 1

    def get_logs(self, resources: Tuple[str], watch: bool, filter_pattern: str) -> None:
        project = self.client.project_path(self.project)

        for element in self.client.list_log_entries([project]):
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

        ago_regexp = (
            r"(\d+)\s?(m|minute|minutes|h|hour|hours|d|day|days|w|weeks|weeks)(?: ago)?"
        )
        ago_match = re.match(ago_regexp, datetime_text)

        if ago_match:
            amount, unit = ago_match.groups()
            amount = int(amount)
            unit = {"m": 60, "h": 3600, "d": 86400, "w": 604800}[unit[0]]
            date = datetime.utcnow() + timedelta(seconds=unit * amount * -1)
        else:
            try:
                date = parse(datetime_text)
            except ValueError:
                raise exceptions.UnknownDateError(datetime_text)

        return date
