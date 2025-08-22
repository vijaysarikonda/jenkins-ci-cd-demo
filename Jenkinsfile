pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/<your-username>/jenkins-ci-cd-demo.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application...'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings -q'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application (simulation)...'
                sh 'python3 app.py'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished. ✅'
        }
        success {
            echo 'Build & Tests Passed 🎉'
        }
        failure {
            echo 'Build Failed ❌'
        }
    }
}
