pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
        IMAGE_NAME = "shrutikwagh/python-jenkins-demo"
    }

    stages {

        stage('Setup Python Environment') {
            steps {
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pytest -v
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                bat """
                docker build -t %IMAGE_NAME%:latest .
                """
            }
        }

        stage('Login to DockerHub') {
            steps {
                bat """
                docker login -u %DOCKERHUB_CREDENTIALS_USR% -p %DOCKERHUB_CREDENTIALS_PSW%
                """
            }
        }

        stage('Push to DockerHub') {
            steps {
                bat """
                docker push %IMAGE_NAME%:latest
                """
            }
        }

        stage('Deploy Locally (Optional)') {
            steps {
                bat """
                docker rm -f python_app || exit 0
                docker run -d --name python_app -p 5000:5000 %IMAGE_NAME%:latest
                """
            }
        }
    }

    post {
        success {
            echo 'Full CI/CD pipeline completed successfully!'
        }
        failure {
            echo 'CI/CD pipeline failed.'
        }
    }
}
