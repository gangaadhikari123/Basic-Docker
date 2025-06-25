# Docker Volume
  Volumes are persistent data stores for containers, created and managed by Docker. You can create a volume explicitly using the docker volume create command, or Docker can create a volume during container or service creation.
- `docker volume`
  - Manage Docker volumes.
  ~~~bash
  docker volume ls                             # List all Docker volumes
  docker volume create my-volume               # Create a new volume
  docker volume inspect my-volume              # Inspect volume details
  docker volume rm my-volume                   # Remove a volume
  docker volume prune                          # Remove all unused volumes
  ~~~
  # 2. LabWork - Docker Volume
  - Git clone the repo
    ```bash
    git clone https://github.com/SATYADAHAL/dockerWorkshop.git
    ```
  - Go to directory `02-docker-Volume`
    ```bash
     cd 02-docker-Volume
    ```
  - And the run this command to build the container.
    ```bash
    docker build -t docker-volume-demo .
    ```
  - Run the container using following command.
    ```bash
    docker run -d -p 8000:8000 -v simple_app_data:/app/data --name simple_volume_container docker-volume-demo
    ```
  - Open browser and go to this url:
    ```bash
    http://localhost:8000
    ```
  - Now stop and container and remove it.
    ```bash
    docker container ls
    docker container stop <container-id>
    docker container rm <container-id>
    ```
  - Again run the container to see the persistent data.
    ```bash
    docker run -d -p 8000:8000 -v simple_app_data:/app/data --name simple_volume_container docker-volume-demo
    ```

# Docker compose
Docker Compose is a tool for defining and running multi-container applications. It is the key to unlocking a streamlined and efficient development and deployment experience.<br>
Compose simplifies the control of your entire application stack, making it easy to manage services, networks, and volumes in a single YAML configuration file. Then, with a single command, you create and start all the services from your configuration file.<br>
Compose works in all environments; production, staging, development, testing, as well as CI workflows. It also has commands for managing the whole lifecycle of your application:
- Start, stop, and rebuild services
- View the status of running services
- Stream the log output of running services
- Run a one-off command on a service
  
# 3. LabWork - Building with docker.
- Git clone the repo
    ```bash
    git clone https://github.com/SATYADAHAL/dockerWorkshop.git
    ```
  - Go to directory `03-react-hot-reload`
    ```bash
    cd 03-react-hot-reload
    ```
  - And the run this command to build the container.
    ```bash
    docker compose up --build
    ```

  - Open browser and go to this url:
    ```bash
    http://localhost:5173
    ```
  - Now Change the contents of file `src/App.jsx` to see live changes.
 
  - Use `ctrl-c` or `docker compose down` to stop the running container.

# 4. LabWork - Building with docker(Volumes and Network).
- Git clone the repo
    ```bash
    git clone https://github.com/SATYADAHAL/dockerWorkshop.git
    ```
  - Go to directory `04-php-myadmin`
    ```bash
    cd 04-php-myadmin
    ```
  - And the run this command to build the container.
    ```bash
    docker compose up --build
    ```
  - And open browser and goto `http://localhost:8080`
