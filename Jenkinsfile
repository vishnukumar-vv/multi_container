pipeline {

    agent { label 'dockergit' }

    environment {
        DOCKER_IMAGE = "8105577060/python-multi"
        DOCKER_TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG -t $DOCKER_IMAGE:latest ./app'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    '''
                }
            }
        }

        stage('Push Image') {
            steps {
                sh '''
                docker push $DOCKER_IMAGE:$DOCKER_TAG
                docker push $DOCKER_IMAGE:latest
                '''
            }
        }

        stage('Deploy Multi Container') {
            steps {
                sh '''
                docker compose down
                docker compose up -d
                '''
            }
        }

    }
}
