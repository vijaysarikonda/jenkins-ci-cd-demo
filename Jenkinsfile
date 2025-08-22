stage('Run New Container') {
    steps {
        sh '''
          docker stop flask-demo || true
          docker rm flask-demo || true
          docker run -d --name flask-demo -p 5050:5050 flask-demo-app
        '''
    }
}
