pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/vijaysarikonda/jenkins-ci-cd-demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-demo-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop flask-demo || true && docker rm flask-demo || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d --name flask-demo -p 5050:5050 flask-demo-app'
            }
        }
    }
}
