# Docker

Start with Docker
| Command                                                              | Description                                                              |
| ---------------------------------------------------------------------| -------------------------------------------------------------------------|
|`Öffnen der CMD im aktuellen Verzeichnis`                             |                                                                          |
|`docker build -t zuul_thalmann .`                                     | `docker build -t zuul_thalmann "PATH"`                                   |
|`docker run -p 8080:8080 -it --name zuul_thalmann -d zuul_thalmann`   |                                                                          |
|`docker exec -it zuul_thalmann /bin/bash`                              | Zuschalten auf den Container                                            |

Start Jenkins with Docker
| Command                                                                                                        | Description                   |
| -------------------------------------------------------------------------------------------------------------- | ------------------------------|
|`docker build -t jenkins_thalmann2 .`                                                                           | Docker Container erstellen    |
|`docker run --name jenkins_thalmann2 --user root --privileged -d -p 8080:8080 -p 50000:50000 jenkins_thalmann2` | Docker Container erstellen    |
|`docker logs jenkins_thalmann2`                                                                                 | fur das Passwor               |
