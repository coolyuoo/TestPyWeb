pipeline {
  agent any
  stages {
    stage('1. 開始部署') {
      steps {
        echo '1. 開始部署'
        powershell 'pwd'
      }
    }
    stage('2. 建置並啟動 Compose 服務') {
      steps {
        // --build 會重新建置 my-fastapi-app:1.0，並自動替換掉舊的 fastapi-container
        bat 'docker compose up -d --build'
      }
    }

  }
}