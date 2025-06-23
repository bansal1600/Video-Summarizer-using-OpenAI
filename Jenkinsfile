pipeline {
  agent any

  environment {
    DOCKER_HUB_USER = credentials('docker-username')         // Jenkins credentials ID
    DOCKER_HUB_PASS = credentials('docker-password')
    IMAGE_TAG = 'latest'
  }

  stages {
    stage('Checkout Code') {
      steps {
        git 'https://github.com/bansal1600/Video-Summarizer-using-OpenAI.git'
      }
    }

    stage('Build and Push Docker Images') {
      steps {
        script {
          docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-credentials') {

            def agentA = docker.build("${DOCKER_HUB_USER}/video_summarizer_using_gemini-agent-a", "agent-a")
            agentA.push("${IMAGE_TAG}")

            def agentB = docker.build("${DOCKER_HUB_USER}/video_summarizer_using_gemini-agent-b", "agent-b")
            agentB.push("${IMAGE_TAG}")

            def ui = docker.build("${DOCKER_HUB_USER}/video_summarizer_using_gemini-ui", "ui")
            ui.push("${IMAGE_TAG}")
          }
        }
      }
    }

    stage('Deploy via Ansible (Optional Now)') {
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
