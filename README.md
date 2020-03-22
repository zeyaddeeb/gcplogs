# gcplogs

![build](https://github.com/zeyaddeeb/gcplogs/workflows/build/badge.svg) ![PyPI - License](https://img.shields.io/pypi/l/gcplogs) ![PyPI](https://img.shields.io/pypi/v/gcplogs) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/gcplogs) [![codecov](https://codecov.io/gh/zeyaddeeb/gcplogs/branch/master/graph/badge.svg)](https://codecov.io/gh/zeyaddeeb/gcplogs)

`gcplogs` is a simple command line tool for querying logging events from [Google Cloud Logging](https://cloud.google.com/logging/docs).

Features
--------

Example
-------

Installation
------------

You can easily install `gcplogs` using `pip` :

``` bash
pip install gcplogs
```

Optional:

``` bash
gcplogs --install-completion
```

Providing credentials to gcplogs
------------------------------------------

Option 1: Follow [recommended way to authenticate Google Cloud API](https://cloud.google.com/docs/authentication/getting-started)

Option 2: If you have an activated service account, just create an environment variable:

``` bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/[FILE_NAME].json"
```

Option 3: If you have gcloud installed, you can use this method, but you might run into rate-limit errors:

``` bash
gcloud auth application-default login
```

Filter options
----------------

You can use `--filter-pattern` if you want to only retrieve logs which match one Stackdriver Logs Filter pattern.

``` bash
gcplogs get audited_resource --filter-pattern="textPayload:10.0.0.0/8" --project google-ai
```

Full documentation of how to write patterns: https://cloud.google.com/logging/docs/view/logging-query-language

Helpful Links
-------------

* https://cloud.google.com/logging/docs/view/logging-query-language

