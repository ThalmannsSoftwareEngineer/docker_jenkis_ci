pipeline {
    agent any

    stages {
        stage('Python') {
            steps {
                // Installiere Python im Container
                sh 'apt-get update && apt-get install -y python3' 
                sh 'pip3 install --upgrade pip' // Pip aktualisieren
                sh 'pip3 install codecoverage' // Codecoverage-Paket installieren
            }
        }
        stage('Checkout') {
            steps {
                // Checkout des Codes aus dem Repository
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                // Ausführen des Python-Skripts
                sh 'python3 /var/jenkins_home/workspace/myPipeline/print_time.py'
            }
        }
        stage('Test') {
            steps {
                // Ausführen des Python-Skripts-Test
                sh 'python3 /var/jenkins_home/workspace/myPipeline/print_time_test.py'
            }
        }
    }
}
