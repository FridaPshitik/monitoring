# monitoring

This repo contains two products:


## elastic-logger

Uploading logs to Elastic \
The product is served as a package installed using Wheels
Uploading is done asynchronously while responding to logs that failed to upload

## elastic-monitoring

Monitoring of http requests and system metrics
The monitoring is performed by upgrading a base image to the nginx-unit image and creating a shell for the existing project that combines the use of metricbeat and filebeat.