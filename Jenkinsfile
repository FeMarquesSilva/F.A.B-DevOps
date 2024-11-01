pipeline {
    agent any

    stages {
        stage('Clonar Repositório') {
            steps {
                git url: 'https://github.com/FeMarquesSilva/F.A.B-DevOps.git', branch: 'main'
            }
        }

        stage('Build com Docker') {
            steps {
                script {
                    // Build da imagem Docker
                    sh 'docker-compose build'
                }
            }
        }

        stage('Subir Contêiner') {
            steps {
                script {
                    // Subir os contêineres
                    sh 'docker-compose up -d'
                }
            }
        }
    }

   }
