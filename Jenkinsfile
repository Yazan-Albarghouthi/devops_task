pipeline {
    agent any

    environment {
        IMAGE_NAME     = 'devops_task'
        IMAGE_TAG      = "build-${env.BUILD_NUMBER}"
        CONTAINER_NAME = "devops_task_app_${env.BUILD_NUMBER}"
        DOCKER_NETWORK = 'jenkins'
        DOCKERHUB_USER = 'yazanalbarghouthi'
    }

    stages {
        stage('Build & Test') {
            steps {
                sh '''
                  echo "Building Docker image $IMAGE_NAME:$IMAGE_TAG"
                  docker build -t $IMAGE_NAME:$IMAGE_TAG .
                '''
            }
        }

        stage('Ephemeral Test Environment') {
            steps {
                sh '''
                  echo "Starting ephemeral test container $CONTAINER_NAME on network $DOCKER_NETWORK"
                  docker run -d --rm \
                    --name $CONTAINER_NAME \
                    --network $DOCKER_NETWORK \
                    $IMAGE_NAME:$IMAGE_TAG

                  echo "Waiting for app to start..."
                  sleep 10

                  echo "Calling /ping endpoint inside the ephemeral environment"
                  curl -f http://$CONTAINER_NAME:8000/ping

                  echo "Stopping test container"
                  docker stop $CONTAINER_NAME || true
                '''
            }
        }

         stage('Push Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-jenkins-token',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                      echo "Logging in to Docker Hub as $DOCKER_USER"
                      echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin

                      REMOTE_IMAGE="$DOCKER_USER/devops_task:$IMAGE_TAG"

                      echo "Tagging local image $IMAGE_NAME:$IMAGE_TAG as $REMOTE_IMAGE"
                      docker tag $IMAGE_NAME:$IMAGE_TAG $REMOTE_IMAGE

                      echo "Pushing image $REMOTE_IMAGE to Docker Hub"
                      docker push $REMOTE_IMAGE

                      echo "Logging out from Docker Hub"
                      docker logout
                    '''
                }
            }
        }
    }

    
       post {
        success {
            mail(
                to: 'albarghouthi.yh@gmail.com',
                subject: "Build SUCCESS",
                body: """Commit ID: ${env.GIT_COMMIT ?: 'unknown'}
                Build URL: ${env.BUILD_URL}
                Test summary: Unit tests (pytest in Docker builder stage) + ephemeral /ping check: SUCCESS."""
            )
        }
        failure {
            mail(
                to: 'albarghouthi.yh@gmail.com',
                subject: "Build FAILURE",
                body: """Commit ID: ${env.GIT_COMMIT ?: 'unknown'}
                Build URL: ${env.BUILD_URL}
                Test summary: One or more of the following failed: Docker build / pytest / ephemeral /ping check / push image. Check Jenkins console logs."""
            )
        }
    }

}
