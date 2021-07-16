from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World, version 1.0.0 !"

import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler

logger = logging.getLogger(__name__)

# TODO: replace the all-zero GUID with your instrumentation key.
logger.addHandler(AzureLogHandler(
    connection_string='InstrumentationKey=5c47d0c6-2ae8-4e72-ae9d-2e1cee2be5e1')
)
