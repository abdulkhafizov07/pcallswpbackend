pipeline {
    agent {
        label "python-agent"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                if [ ! -d env ]; then
                    echo "Creating virtual environment"
                    python3 -m venv env
                fi
                make install-dev
                '''
            }
        }

        stage('Format & Lint') {
            steps {
                sh 'make format lint'
            }
        }

        state('Build') {
            steps {
                sh 'make build-db build'
            }
        }

        state('Test') {
            steps {
                sh 'make test'
            }
        }

        stage('Clean') {
            steps  {
                sh 'make clean'
            }
        }

        state('Deploy') {
            steps {
                echo "Deploy here"
            }
        }
    }
}