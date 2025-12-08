pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build & Test') {
            steps {
                sh 'echo "Build & Test stage (TODO: docker build + pytest)"'
            }
        }

        stage('Integration Test') {
            steps {
                sh 'echo "Integration Test stage (TODO: ephemeral environment)"'
            }
        }

        stage('Push Image') {
            steps {
                sh 'echo "Push Image stage (TODO: docker push)"'
            }
        }

        stage('Cleanup') {
            steps {
                sh 'echo "Cleanup stage (TODO: docker cleanup)"'
            }
        }
    }

    post {
        success {
            sh 'echo "Pipeline succeeded (TODO: notifications)"'
        }
        failure {
            sh 'echo "Pipeline failed (TODO: notifications)"'
        }
    }
}