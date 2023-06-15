// JenkinsFile
pipeline {
    // agent
    agent any

    // stages
    stages {
        stage('Checkout') {
            steps {
                // Checkout des Codes aus dem Repository
                checkout scm
            }
        }
        stage('Build') {
            steps {
                // Ausführen des Python-Skripts
                sh 'python3 print_time.py'
            }
        }
        stage('Test') {
            steps {
                // Ausführen des Python-Skripts-Test
                sh 'python3 print_time_test.py'
            }
        }
         stage('Ausgabe') {
            steps {
                // Benutzerausgabe
                echo "Running ${env.BUILD_NUMBER} on ${env.JENKINS_URL}"
                echo "Run was successful!"
            }
        }
    }
}

