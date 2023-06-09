pipeline {
    agent any

    stages {
        // stage('Install Python & PIP') {
        //     steps {
        //         // Installiere Python im Container
        //         sh 'apt-get update && apt-get install -y python3' 
        //         sh 'apt install -y python3-pip'
        //         sh 'pip install coverage'
        //     }
        // }
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
                sh 'python3 /var/jenkins_home/workspace/myPipeline/print_time_test.py'
            }
        }
    }
}
