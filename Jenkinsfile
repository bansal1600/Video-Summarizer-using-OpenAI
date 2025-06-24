pipeline {
  agent any

  environment {
    IMAGE_TAG = 'latest'
  }

  stages {
    stage('Checkout') {
      steps {
        git credentialsId: 'github-creds', url: 'https://github.com/bansal1600/Video-Summarizer-using-OpenAI.git', branch: 'main'
      }
    }

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

   stage('Deploy to Kubernetes') {
      steps {
        withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {
          sh '''
            kubectl apply -f k8s/agent-a-deployment.yaml
            kubectl apply -f k8s/agent-b-deployment.yaml
            kubectl apply -f k8s/ui-deployment.yaml
          '''
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
