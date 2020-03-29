..gcplogs documentation master file, created by
   sphinx-quickstart on Sat Mar 21 17:13:32 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to gcplogs's documentation!
===================================

Examples
-------

``` bash
gcplogs get gce_instance --event-start='1 week ago'
```

``` bash
gcplogs get gce_instance --event-start='1 min ago' --watch
```

More advanced example:

``` bash
gcplogs get ml_job --event-start '2 mins ago' --filter-pattern 'protoPayload:unicorns'
```

``` bash
gcplogs get ml_job --event-start '2 mins ago' --filter-pattern 'protoPayload:unicorns' --project 'rainbows' --credentials '/cool-kids.json'
```

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
