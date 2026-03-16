pipeline {

    agent any

    environment {
        DOCKER_IMAGE = "vishnu/python-multi"
        CONTAINER_NAME = "pythonmulti"
    }

    stages {

        stage('Git Checkout') {
            steps {
                git 'https://github.com/yourrepo/python-multi-ci.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE ./app'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                docker login -u YOUR_DOCKER_USER -p YOUR_DOCKER_PASS
                docker push $DOCKER_IMAGE
                '''
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
