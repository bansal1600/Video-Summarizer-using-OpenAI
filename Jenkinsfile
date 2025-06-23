pipeline {
  agent any

  environment {
    IMAGE_TAG = 'latest'
  }

  options {
    skipDefaultCheckout(true)
  }

  stages {
    stage('Checkout Code') {
      steps {
        git credentialsId: 'github-creds', url: 'https://github.com/bansal1600/Video-Summarizer-using-OpenAI.git', branch: 'main'
      }
    }

    stage('Build and Push Docker Images') {
      steps {
        script {
          withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
            docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-credentials') {
              def agentA = docker.build("${DOCKER_USER}/video_summarizer_using_gemini-agent-a:${IMAGE_TAG}", "agent-a")
              agentA.push()

              def agentB = docker.build("${DOCKER_USER}/video_summarizer_using_gemini-agent-b:${IMAGE_TAG}", "agent-b")
              agentB.push()

              def ui = docker.build("${DOCKER_USER}/video_summarizer_using_gemini-ui:${IMAGE_TAG}", "ui")
              ui.push()
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
