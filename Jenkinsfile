pipeline {

    agent { label 'dockergit' }

    environment {
        DOCKER_IMAGE = "8105577060/python-multi"
        DOCKER_TAG = "latest"
    }

    stages {

        stage('Git Checkout') {
            steps {
                git 'https://github.com/vishnukumar-vv/multi_container.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG ./app'
            }
        }

        stage('Docker Login') {
            steps {
                sh '''
                docker login -u 8105577060 -p YOUR_DOCKER_PASSWORD
                '''
            }
        }

        stage('Push Image to DockerHub') {
            steps {
                sh 'docker push $DOCKER_IMAGE:$DOCKER_TAG'
            }
        }

        stage('Deploy Multi Container') {
            steps {
                sh '''
                docker-compose down
                docker-compose up -d
                '''
            }
        }

    }

}
