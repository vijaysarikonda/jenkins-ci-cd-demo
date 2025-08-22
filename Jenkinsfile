pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-demo-app"
        CONTAINER_NAME = "flask-demo"
        PORT = "5050"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/vijaysarikonda/jenkins-ci-cd-demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Stop & Remove Old Container') {
            steps {
                sh 'docker rm -f $CONTAINER_NAME || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d --name $CONTAINER_NAME -p $PORT:$PORT $IMAGE_NAME'
            }
        }
    }
}
