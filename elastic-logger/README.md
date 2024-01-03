# infinity-elastic-logs

This project is a Python logging library that integrates with Elasticsearch for centralized logging. It provides a simple and convenient way to send logs to Elasticsearch with different log levels.

## Installation

 [The binary installation file](infinity_elastic_logs-0.0.0-py3-none-any.whl) attached to this repository should be taken,
Attach to the project where it will be used
and install with:

```bash
pip install path/to/infinity_elastic_logs-0.0.0-py3-none-any.whl
```

Replace path/to/infinity_elastic_logs-0.0.0-py3-none-any.whl with the path where the file is located in your project.

## Usage

To use the logging library, follow these steps:

1. Import the `ElasticLogger` class:

    ```python
    from infinity_elastic_logs.elastic_logger import ElasticLogger
    ```

2. Create an instance of the ElasticLogger class, providing a service name:

    ```python
    logger = ElasticLogger("my-service")
    ```

3. Use the different log levels to send logs:

   ```python
    logger.debug("This is a debug log")
    logger.info("This is an info log")
    logger.warning("This is a warning log")
    logger.error("This is an error log")
    logger.critical("This is a critical log")
    ```

## Configuration

1. **Environment Variables**

    The Elastic Logger project relies on environment variables for configuration. Before running the project, make sure to set the following environment variables:

    - CLOUD_ID: The Cloud ID of your Elasticsearch instance.
    - NAME: The username for authentication with Elasticsearch.
    - PASSWORD: The password for authentication with Elasticsearch.
    - INDEX: The name of the Elasticsearch index where logs will be stored.
    - FAILED_LOGS_FILE_PATH (optional): The file path for storing failed logs locally. If not provided, the default path failed_logs/failed_logs.log will be used.

    for example, you can export on the terminal:

    ```bash
    export CLOUD_ID=<replace to your cloud id>
    export NAME=<replace to your username>
    export PASSWORD=<replace to your password>
    export INDEX=<replace to the name of the Elasticsearch index>
    ```

2. **Elasticsearch Connection**

    The ElasticsearchConnection class handles the connection to Elasticsearch. Ensure that the environment variables mentioned above are correctly set before running the project. The connect_elasticsearch method establishes a connection to Elasticsearch using the provided credentials. If the connection fails, an exception will be raised.

3. **Log Format**

   The logs sent to Elasticsearch have the following format:

   ```json
   {
    "timestamp": "<current_timestamp>",
    "message": "<log_message>",
    "level": "<log_level>",
    "service": "<service_name>"
    }
    ```

4. **Failed Logs**

    if uploading a log to Elasticsearch fails, the logs will be written to a local file specified by the FAILED_LOGS_FILE_PATH environment variable. If the variable is not set or the defined path does not exist, the default path failed_logs/failed_logs.log will be used. When the connection is successful again, the local log file will also be uploaded to Elasticsearch.
