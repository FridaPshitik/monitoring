# Monitoring Project

This project serves as a template for monitoring HTTP requests in FastAPI services using NGINX Unit, Filebeat, and Metricbeat. The FastAPI application is located in the monitoring/nginx-unit/webapp/ directory.

## Project Structure

The project structure is as follows:

```structure
monitoring/
├── filebeat/
│   └── filebeat.yml
├── metricbeat/
│   └── metricbeat.yml
├── nginx-unit/
│   └── config/
│       └── config.json
│   └── webapp/
├── docker-compose.yml
└── README.md    
```

The `nginx-unit` directory contains the configuration files for ngix unit, including the `config.json` file. The FastAPI application is located in the `webapp` directory.

The `filebeat` directory contains the `filebeat.yml` configuration file, which specifies the log paths and Elasticsearch output settings.

The `metricbeat` directory contains the `metricbeat.yml` configuration file, which includes the Docker module settings and Elasticsearch output settings.

The `docker-compose.yml` file defines the services and their configurations for running the monitoring project.

## Prerequisites

Before getting started, make sure you have the following installed:

- Docker
- Docker Compose

## Installation

1. Clone this repository.
2. Navigate to the project directory.
3. Modify the configuration files according to your requirements.
4. Build and start the containers using Docker Compose:

   ```bash
   docker-compose up -d
   ```

5. Access your fast-api application at <http://localhost:8000> (or another port if you changed).

## Configuration

**environments**
To set the elastic account to which the logs will be uploaded for monitoring, you will need to set the following environment variables:

- `ELASTICSEARCH_HOST`: The host of your Elasticsearch instance, e.g. "http://<the-cluster-id>.us-central1.gcp.cloud.es.io:443".
- `ELASTIC_USERNAME`: The username for the Elasticsearch account
- `ELASTIC_PASSWORD`: The password for the Elasticsearch account
- `ELASTICSEARCH_INDEX`: The index to which filebeat logs will be written.

**ngix unit**
Configuration file: nginx-unit/config.json
Open the nginx-unit/config/config.json file and modify the configuration according to your requirements. Make sure to set the correct path for the FastAPI app in the applications/webapp section, Be sure to place your fastapi application inside the nginx-unit/webapp directory.

**filebeat**
Configuration file: filebeat/filebeat.yml
Defining the Elasticsearch account to which the logs will be uploaded is according to the following environment variables:\
ELASTICSEARCH_HOST , ELASTICSEARCH_USERNAME , ELASTICSEARCH_PASSWORD , ELASTICSEARCH_INDEX.

**metricbeat**
Configuration file: metricbeat/metricbeat.yml
The definition of the Elasticsearch account to which the indices will increase is according to the following environment variables:\
ELASTICSEARCH_HOST , ELASTICSEARCH_USERNAME , ELASTICSEARCH_PASSWORD.

## Monitor the FastAPI services

- Nginx Unit: The FastAPI app is accessible at <http://localhost:8000>, You can send HTTP requests to this endpoint and monitor the logs in the Nginx Unit access log file located at nginx-unit/log/unit/access.log.

- Filebeat: Filebeat will collect the logs from the Nginx Unit access log file and send them to Elasticsearch. You can view the logs in Kibana or any other Elasticsearch log viewer.

- Metricbeat: Metricbeat will collect CPU and container metrics from the Nginx Unit container and send them to Elasticsearch. You can view the metrics in Kibana or any other Elasticsearch metric viewer.