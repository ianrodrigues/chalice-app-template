import sentry_sdk
from sentry_sdk.integrations import aws_lambda, chalice

from chalicelib import settings


def configure_sentry() -> None:
    """
    Configure Sentry with AWS Lambda and Chalice integration.
    """
    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        integrations=[
            aws_lambda.AwsLambdaIntegration(timeout_warning=True),
            chalice.ChaliceIntegration(),
        ],
        traces_sample_rate=1.0,
        environment=settings.CHALICE_STAGE,
    )
