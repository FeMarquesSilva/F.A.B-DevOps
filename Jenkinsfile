pipeline {
    agent any
    
    stages {
        stage('Checkout Code') {
            steps {
                // Faz o checkout do código da branch main
                git branch: 'main', url: 'https://github.com/FeMarquesSilva/F.A.B-DevOps'
            }
        }
        
        stage('Build Docker Images') {
            steps {
                dir('docker-project') {
                    // Comando para construir as imagens dos containers
                    sh 'docker-compose build'
                }
            }
        }
        
        stage('Clean Up') {
            steps {
                script {
                    // Para e remove containers antigos, evitando conflito de nomes
                    dir('docker-project') {
                        sh 'docker-compose down || true'
                    }
                }
            }
        }

        stage('Run Containers') {
            steps {
                dir('docker-project') {
                    // Comando para iniciar os containers em segundo plano
                    sh 'docker-compose up -d'
                }
            }
        }
        
        stage('Check Application Status') {
            steps {
                script {
                    // Verifica se a aplicação está acessível em localhost:5000
                    echo "Aplicação Flask disponível em http://localhost:5000"
                    // Aqui você pode adicionar um comando para verificar o status do container, se necessário
                }
            }
        }
    }
}

