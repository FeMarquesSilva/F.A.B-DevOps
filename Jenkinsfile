pipeline {
    agent any

    stages {
        stage('Clonar Repositório') {
            steps {
                git url: 'https://github.com/FeMarquesSilva/F.A.B-DevOps', branch: 'main'
            }
        }

        stage('Executar Script') {
            steps {
                sh '''
                    chmod +x ./automatizador.sh  # Garante que o script seja executável
                '''
            }
        }
    }
}

