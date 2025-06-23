pipeline {More actions
  agent any

  environment {
    IMAGE_TAG = 'latest'
  }

  stages {

    stage('Build and Push Docker Images') {
      steps {
        script {
          withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
            docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-credentials') {

              def agentA = docker.build("${DOCKER_USER}/video_summarizer_using_gemini-agent-a", "agent-a")
              agentA.push("${IMAGE_TAG}")

              def agentB = docker.build("${DOCKER_USER}/video_summarizer_using_gemini-agent-b", "agent-b")
              agentB.push("${IMAGE_TAG}")

              def ui = docker.build("${DOCKER_USER}/video_summarizer_using_gemini-ui", "ui")
              ui.push("${IMAGE_TAG}")
            }
          }
        }
      }
    }

    stage('Deploy via Ansible (Optional)') {
      steps {
        script {
          sh 'ansible-playbook ci-cd/deploy.yml'
        }
      }
    }
  }

  post {
    always {
      echo "Pipeline completed!"
    }
  }
}