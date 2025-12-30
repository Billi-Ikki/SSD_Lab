pipeline {
    agent any
    
    environment {
        APP_NAME = 'flask-app'
        DOCKER_IMAGE = "${APP_NAME}:${BUILD_NUMBER}"
    }
    
    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Billi-Ikki/SSD_Lab'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest -v
                '''
            }
        }
        
        stage('Build App') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }
        
        stage('Deploy App') {
            steps {
                sh '''
                    docker stop ${APP_NAME} || true
                    docker rm ${APP_NAME} || true
                    docker run -d -p 5000:5000 --name ${APP_NAME} ${DOCKER_IMAGE}
                '''
            }
        }
    }
    
    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}