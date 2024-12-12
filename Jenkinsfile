pipeline {
    agent any

    environment {
        
        docker_image = 'incident_management-web'
        // DOCKER_REGISTRY = 'your-docker-registry' // optional if pushing to Docker Hub or private registry
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from Git repository
                git branch: 'main', credentialsId: '3b839c49-a8ba-4057-882d-8be0e139525c', url: 'https://github.com/Shubh1321/incident_management.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image using the Dockerfile
                    bat 'docker build -t ${docker_image} .'
                }
            }
        }

        // stage('Run Tests') {
        //     steps {
        //         script {
        //             // Run the Django tests in Docker (assuming you have test cases)
        //             bat 'docker run --rm docker_image python manage.py test'
        //         }
        //     }
        // }

        // stage('Push Docker Image') {
        //     when {
        //         branch 'main'
        //     }
        //     steps {
        //         script {
        //             // Log in to Docker registry (optional)
        //             // sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD $DOCKER_REGISTRY'
        //             // Push the image to Docker registry (optional)
        //             // sh 'docker push $DOCKER_IMAGE'
        //         }
        //     }
        // }

        stage('Deploy') {
            steps {
                script {
                    // Example for deploying via Docker (this could be specific to your environment)
                    bat 'docker run -d -p 8000:8000 ${docker_image}'
                }
            }
        }
    }

    post {
        always {
            // Clean up after build (remove Docker images, containers, etc.)
            bat 'docker system prune -f'
        }
    }
}
