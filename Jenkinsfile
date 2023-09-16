pipeline {
    agent any
    environment {
        version = 'V1'
    }
    stages {
        stage('Download Code from GHub') {
            steps {
                sh 'git clone https://github.com/cobidennis/nationapp.git'
            }
        }
        stage ('Build Image') {
            steps {
                sh '''
                    cd containers101
                    docker build -t cobidennis/nationapp:$version .
                '''
            }
        }
        stage ('Push Image to DHub') {
            steps {
                withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId:'docker', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD']]) {
                    sh '''
                        docker login -u $USERNAME -p $PASSWORD
                        docker push cobidennis/nationapp:$version
                    '''
                } 
            }
        }
        stage ('Deploy App') {
            steps {
                sh '''
                    docker rm -f nationapp | echo ""
                    docker run -d --name nationapp --rm -p 5000:5000 cobidennis/nationapp:$version
                '''
            }
        }
    }
    post {
        always {
            deleteDir()
        }
    }
}