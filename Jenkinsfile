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

        stage('Executar Testes') {
            steps {
                script {
                    // Executar os testes (caso tenha)
                    sh 'docker-compose run --rm app python -m unittest discover'
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

    post {
        success {
            echo 'Build realizado com sucesso!'
        }
        failure {
            echo 'Ocorreu um erro no build.'
        }
    }
}
