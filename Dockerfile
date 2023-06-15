# Basisimage mit Java und Jenkins
FROM jenkins/jenkins

# Als Root-Benutzer wechseln
USER root

# Python und Pip installieren
RUN apt-get update && apt-get install -y python3
RUN apt install -y python3-pip

# Coverage installieren
RUN pip3 install coverage

# Install plugins using jenkins-plugin-cli
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli --plugins < /usr/share/jenkins/ref/plugins.txt

# Benutzer zurückwechseln
USER jenkins
# Exponieren des Jenkins-Webinterfaces
EXPOSE 8080
