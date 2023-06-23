// JenkinsFile
pipeline {
    // agent
    agent any
    // stages
    stages {
        stage('Clean Up') {
            steps {
                // Clean Up
                deleteDir()
                echo "delete dir was successful!"
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
         stage('Build Remote') {
            steps {
                // Trigger func-Pipline mit einem Übergabeparameter
                build job: 'func', parameters: [[$class: 'booleanParamValue', name: 'myBoolean', value: true]]
            }
        }
    }
}

