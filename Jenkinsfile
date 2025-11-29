pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/<your-username>/<your-repo>.git'
            }
        }

        stage('Setup Python') {
            steps {
                sh """
                python -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                . venv/bin/activate
                pytest -v
                """
            }
        }

        stage('Build Docker Image') {
            when {
                branch 'main'
            }
            steps {
                sh """
                docker build -t python-jenkins-demo .
                """
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
