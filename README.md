# AWS Chalice Skeleton

This skeleton can be used to scaffold a [Chalice application](https://aws.github.io/chalice/#). Follow these steps to get started:

1. Run `python configure.py` to replace all placeholders throughout all the files.

## AWS Chalice

Chalice is a framework for writing serverless apps in python. It allows you to create and deploy applications that use AWS Lambda quickly. It provides:

* A command line tool for creating, deploying, and managing your app
* A decorator-based API for integrating with Amazon API Gateway, Amazon S3, Amazon SNS, Amazon SQS, and other AWS services.
* Automatic IAM policy generation

Learn more on the [GitHub repository](https://github.com/aws/chalice) or [Chalice documentation](https://aws.github.io/chalice/).

## Settings

The settings file structure is inspired in [Django Settings](https://docs.djangoproject.com/en/4.1/topics/settings/).

Below there's a list of settings available and their default values:

### `CHALICE_DEBUG`

Default: `False`

A boolean that turns on/off debug mode.

### `CHALICE_STAGE`

Default: `dev`

Chalice has the concept of [stages](https://aws.github.io/chalice/topics/stages.html), which are entirely separate sets of AWS resources.

However, the stage name is not available for reference in the project code. An alternative solution is to define an environment variable with the same name as the stage.

> `CHALICE_STAGE` does not interfere in the actual Chalice stage, and vice-versa. It's your responsibility to keep both in sync.

### `LOGGING`

Default: A dictionary of [logging settings](https://docs.python.org/3/library/logging.config.html#logging-config-dictschema).

It's a data structure containing configuration information. See also [Logging](#logging-1).

### `SENTRY_DSN`

Default: `None`

A DSN tells a Sentry SDK where to send events so the events are associated with the correct project.

If an SDK is not initialized or if it is initialized with an empty DSN (default behavior), the SDK will not send any data over the network, such as captured exceptions.

## Logging

By default, this skeleton uses Python's standard [logging](https://docs.python.org/3/library/logging.html#module-logging) module.

```py
from logging import getLogger

logger = getLogger(__name__)
logger.info("Loading module [%s].", __name__)


def demo():
    logger.info("Processing function [%s.demo].", __name__)
    return True
```

To configure logging, you use [`LOGGING`](#logging) to define a dictionary of [logging settings](https://docs.python.org/3/library/logging.config.html#logging-config-dictschema). These settings describe the loggers, handlers, filters, and formatters you want in your logging setup and the log levels and properties you want those components to have.

This skeleton configures logging as part of the project initialization. Therefore, you can be sure that loggers are always ready for use.

## Sentry

Sentry is a developer-first error tracking and performance monitoring platform that helps developers see what matters, solve quicker, and learn continuously about their applications.

This skeleton configures Sentry out of the box with [Chalice](https://docs.sentry.io/platforms/python/guides/chalice/) and [AWS Lambda](https://docs.sentry.io/platforms/python/guides/aws-lambda/) integrations; you only have to set [`SENTRY_DSN`](#sentry_dsn) in the settings.py file.
