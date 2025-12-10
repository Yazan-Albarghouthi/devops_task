pipeline {
    agent any

    environment {
        IMAGE_NAME = 'devops_task'
        IMAGE_TAG  = "build-${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build & Test') {
            steps {
                sh '''
                  echo "Building Docker image $IMAGE_NAME:$IMAGE_TAG"
                  docker build -t $IMAGE_NAME:$IMAGE_TAG .
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
