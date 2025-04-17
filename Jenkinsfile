pipeline {
    any agents
    stages {
        stage {'Chechout code'} {
            steps {
                git credentialsId: "MY_PAT", url: "https://github.com/gayathri7022/Test.git", branch: "main"
            }
        }
        stage ('Install dependencies') {
            steps {
                bat '''
                   "C:\\Users\\mjmnj\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m venv venv
                    call .\\venv\\Scripts\\activate
                    pip install -upgrade pip
                    pip install pytest
                   '''
            }
        }
        stage ('Test') {
            bat '''
                call .\\venv\\Scripts\\activate
                pytest test.py
                '''
        }
        stage ('Deploy') {
            echo "Deploying feature"
            bat '''
                call .\\venv\\Scripts\\activate
                "C:\\Users\\mjmnj\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" Prime.py
                '''
        }
    }
    post {
            success {
                echo 'pipeline succeded'
            }
            failure {
                echo 'pipeline failed'
             }
        }
}