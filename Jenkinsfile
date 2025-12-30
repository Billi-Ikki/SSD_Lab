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
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate.bat
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                bat '''
                    call venv\\Scripts\\activate.bat
                    pytest -v
                '''
            }
        }
        
        stage('Build App') {
            steps {
                script {
                    bat "docker build -t ${APP_NAME}:${BUILD_NUMBER} ."
                }
            }
        }
        
        stage('Deploy App') {
            steps {
                script {
                    bat """
                        docker stop ${APP_NAME} 2>nul || echo Container not running
                        docker rm ${APP_NAME} 2>nul || echo Container not found
                        docker run -d -p 5000:5000 --name ${APP_NAME} ${APP_NAME}:${BUILD_NUMBER}
                    """
                }
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