Based on the attached `environment_airq_measurand.csv` file:

## API

Create an API REST. 

- Choose your preferred coding language / framework, or the ones that fit better in this context.
- `environment_airq_measurand.csv` is composed of simulated data coming from air quality measurements that were used during the development phase of a well known project for managing Smart Cities. Dataset fields:

   - `Timestamp`: measures are taken every 15’.
   - `id_entity`: quality air station identifier.
   - `so2`: μg/m3 of SO2 (Sulfur dioxide).
   - `no2`: μg/m3 of NO2 (Nitrogen dioxide).
   - `co`: mg/m3 of CO (Carbon monoxide).
   - `o3`: μg/m3 of O3 (Ozone).
   - `pm10`: μg/m3 of PM10 (particulate matter with 10 μm or less in diameter).
   - `pm2_5`: μg/m3 of PM2,5 (particulate matter with 2,5 μm or less in diameter).

### API tasks
- Load de CSV into a PostgreSQL database
- Create an endpoint `/air_quality` that delivers the CSV data in a well structured JSON
- Create a script/tool that creates an API Docker image. Bear in mind that the docker image will be deployed to the production environment at some point, so it must be ready to be deployed on Kubernetes, or any other container environment. Please, explain your deployment choice here.
- Provide a docker-compose environment: it must include a tool and instructions to load the CSV data the first time it runs.

## CI (Continuous Integration)

Elaborate on how to build a CI within this project, in order to deploy the API using GitHub and a cloud provider of your choice.

- A pull request in the master branch must be deployed to the production environment.
- A pull request to the staging branch must be deployed to the staging environment.
- A pull request to the development branch must be deployed to the dev environment.

Please explain in detail how this would work and any technology involved in the process.

## Deployment

The preferred choice here is Kubernetes, but it is not mandatory, so if you pick any other solutions, please explain your choice and why you chose it.

Requirements
- 5 x API containers
- 1 x Database container (redundancy is not mandatory) 
- 1 x Cache container: it should be deployed as an API cache, so once a response is cached, subsequent requests will be served from cache content. Please elaborate your technology choice and any knowledge about caches and invalidation strategies.
**NOTE**: changing the API code it’s not a requirement for implementing the cache layer.
- Provide YAML files (api, cache and db) for k8s, or the suitable configuration files for other technologies, along with instructions on how to use them.
- The provided solution must include all the required dependencies and detailed instructions for the deployment. **i.e**: `kubectl apply -f <file.yaml>`

## Monitoring, logs and backup

Explain and/or provide the components/technologies required to cover a full monitoring, logs and backup system. An operator should be able to diagnose and detect issues with the tools provided.