pipeline {
    agent any

    environment {
        IMAGEN     = 'hola-mundo-devsecops'
        CONTENEDOR = 'hola-mundo-test'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Construyendo la imagen Docker...'
                bat "docker build -t %IMAGEN%:%BUILD_NUMBER% ."
            }
        }

        stage('Test') {
            steps {
                echo 'Ejecutando pruebas unitarias dentro del contenedor...'
                bat "docker run --rm %IMAGEN%:%BUILD_NUMBER% python -m unittest -v"
            }
        }

        stage('Deploy') {
            steps {
                echo 'Desplegando en el entorno de prueba...'
                bat "docker rm -f %CONTENEDOR% 2>nul || exit 0"
                bat "docker run -d --name %CONTENEDOR% -p 5000:5000 %IMAGEN%:%BUILD_NUMBER%"
            }
        }
    }

    post {
        success {
            echo 'Despliegue exitoso: abre http://localhost:5000'
        }
        failure {
            echo 'El pipeline fallo. Revisa la etapa marcada en rojo.'
        }
    }
}
