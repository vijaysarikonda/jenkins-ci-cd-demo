pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/vijaysarikonda/jenkins-ci-cd-demo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh './venv/bin/python -m unittest discover -s . -p "test_*.py"'
            }
        }

        stage('Build') {
            steps {
                echo 'Build stage placeholder (e.g., docker build, package app, etc.)'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploy stage placeholder (copy files, run docker, etc.)'
            }
        }
    }
}
