import sentry_sdk
from sentry_sdk.integrations.excepthook import ExcepthookIntegration


def init_sentry():
    sentry_sdk.init(
        dsn="https://edfb0bb6382303bde30f536bc9f505d1@o4506595548725248.ingest.sentry.io/4506595858251776",
        traces_sample_rate=1.0,
        profiles_sample_rate=1.0,
        integrations=[ExcepthookIntegration()]
    )
