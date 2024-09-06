pipeline {
    agent any
    stages {
        stage('Clonar repositorio') {
            steps {
                git 'https://github.com/Guadamuzz17/dependency.git'
            }
        }
        stage('Instalar dependencias') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Análisis de Vulnerabilidades con Dependency Track') {
            steps {
                 dependencyTrackPublisher artifact: '**/requirements.txt', projectId: '62141afc-37b9-4021-a425-8b0f9907ba8d'
            }
        }
    }
}
