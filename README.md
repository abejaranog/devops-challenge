# DevOps challenge: Solutions
Here you will found the explain for solutions proposed by **Alejandro Bejarano Gómez**

## API
### API tasks
- Load de CSV into a PostgreSQL database 
- Create an endpoint `/air_quality` that delivers the CSV data in a well structured JSON
- Create a script/tool that creates an API Docker image. Bear in mind that the docker image will be deployed to the production environment at some point, so it must be ready to be deployed on Kubernetes, or any other container environment. Please, explain your deployment choice here.
- Provide a docker-compose environment: it must include a tool and instructions to load the CSV data the first time it runs.

### API Solutions
I have chosen Flask as framework because it is the one I feel most comfortable working with.
For this I needed the SQLAlchemy libraries and to create a Model class to make queries to the database. To get the data as JSON I used a serializer class that transforms the table view into a JSON-serializable object.
Also, I have dockerized the database and seeded it on entrypoint to make easier the future compose environment creation.
The docker-compose environment builds both Dockerfiles and deploys a cluster ready to use. I have used an .env file to save sensitive data and added a .gitignore to avoid the upload of this file.

## CI (Continuous Integration)
### CI TASKS
Elaborate on how to build a CI within this project, in order to deploy the API using GitHub and a cloud provider of your choice.

- A pull request in the master branch must be deployed to the production environment.
- A pull request to the staging branch must be deployed to the staging environment.
- A pull request to the development branch must be deployed to the dev environment.

Please explain in detail how this would work and any technology involved in the process.

### CI Solutiones
Note: If there were two environments in cloud, I would use local enviroment as development. 

For the CI of this project I would use a Jenkins and Gitlab based environment that would have this workflow:

Pull a branch from the develop branch that contains the type of change in the name: (example: feature/..., fix/...) and perform PULL REQUEST to develop. Once approved, it would launch the development environment deployment job through a webhook to perform a continuous deployment, to make easier the development task. 

To perform the PR from development to staging, I would perform a series of unit tests related to syntax, best practices and functional. From here the job would be deployed by hand.

To deploy in the production environment, a PR should be done from staging to the master branch and pass a series of tests related to standardization (That it is documented, etc).

Once the code is in master, a release should be tagged to perform the deployment from Jenkins, which should accept the release as an external parameter. This way we ensure a rollback possibility in case of failure in production.
This job should be launched manually, with more control of who and when it is launched.

## Deployment
### Deployment tasks
The preferred choice here is Kubernetes, but it is not mandatory, so if you pick any other solutions, please explain your choice and why you chose it.

Requirements
- 5 x API containers
- 1 x Database container (redundancy is not mandatory) 
- 1 x Cache container: it should be deployed as an API cache, so once a response is cached, subsequent requests will be served from cache content. Please elaborate your technology choice and any knowledge about caches and invalidation strategies.
**NOTE**: changing the API code it’s not a requirement for implementing the cache layer.
- Provide YAML files (api, cache and db) for k8s, or the suitable configuration files for other technologies, along with instructions on how to use them.
- The provided solution must include all the required dependencies and detailed instructions for the deployment. **i.e**: `kubectl apply -f <file.yaml>`

### Deployment solutions

To deploy it on kubernetes, I decided to make 4 yaml manifest:

First manifest contains the Secrets object thats manage sensible information.

Second manifest contains the psql deployment and its service to expose it. It could be done with a StatefulSet, but in this case that API only query a "select" clause, I decided to use a deployment object.

Third manifest deploys the api and its service and fourth, redis cache and its service.

To apply this deployments, it was necessary build the dockerfiles again and push to my GCR repository.

To test all the environment, I used *kubectl port forwarding* to create a port map between the cluster and my localhost port.

Finally, to deploy all files, I decided to use a *kustomization* yaml file.
To deploy the cluster, you must run *kubectl apply -k .* in *kubernetes-env* folder.

## Monitoring, logs and backup
### Monitoring tasks
Explain and/or provide the components/technologies required to cover a full monitoring, logs and backup system. An operator should be able to diagnose and detect issues with the tools provided.

### Monitoring Solutions
To monitor this cluster solution, I would use the solution Prometheus+Grafana, to make a end-to-end alert system combined with a DaemonSet which any fluentd system to cover logs upload (Elasticsearch, Stackdriver, AWS Cloudwatch...).
It's enough with the ReplicaSets applied to be covered about backups on this cluster, but, if we need to write on database, I would use a persistent volume with a StatefulSet to be covered.

## Additional notes
Thanks for reading my proposal for this challenge.
I hope you like it!

@ Alejandro Bejarano Gómez
