#!/usr/bin/env groovy

pipeline {
  agent any

  options {
    timeout(time: 15, unit: 'MINUTES')
  }

  triggers {
    cron('H 2 * * *')
  }

  environment {
    GMT_COMPOSE_FILE = 'gmt-docker-compose.yml'
    GMT_HTTP_PORT = "18090"
    PARTICLES_EXPORT_URL = "http://127.0.0.1:${GMT_HTTP_PORT}/winery/servicetemplates"
  }

  stages {
    stage('Ensure clean and up to date environment') {
      steps {
        cleanWs()
        sh "docker-compose -f ${GMT_COMPOSE_FILE} rm -fsv"
        sh "docker-compose -f ${GMT_COMPOSE_FILE} pull"
      }
    }
    stage('Set up and start GMT') {
      steps {
        sh "chmod -R a+rwx ."
        sh "docker-compose -f ${GMT_COMPOSE_FILE} up -d"
        sh "sleep 30"
      }
    }
    stage('Obtain radon.blueprints Service Templates') {
      matrix {
        axes {
          axis {
            name 'SERVICE_TEMPLATE'
            values 'SockShopTestingExample', 'ThumbnailGeneration'
          }
          axis {
            name 'NAMESPACE'
            values 'radon.blueprints'
          }
        }
        stages {
          stage('Query Service Template') {
            environment {
              CSAR = "${NAMESPACE}.${SERVICE_TEMPLATE}.csar"
            }
            steps {
              sh "curl -H 'Accept: application/xml' -o \"${CSAR}\" \"${PARTICLES_EXPORT_URL}/${NAMESPACE}/${SERVICE_TEMPLATE}/?yaml&csar\""
              archiveArtifacts artifacts: "${CSAR}", onlyIfSuccessful: true
            }
          }
        }
      }
    }
    stage('Obtain radon.blueprints.testing Service Templates') {
      matrix {
        axes {
          axis {
            name 'SERVICE_TEMPLATE'
            values 'JMeterMasterOnly', 'DeploymentTestAgent'
          }
          axis {
            name 'NAMESPACE'
            values 'radon.blueprints.testing'
          }
        }
        stages {
          stage('Query Service Template') {
            environment {
              CSAR = "${NAMESPACE}.${SERVICE_TEMPLATE}.csar"
            }
            steps {
              sh "curl -H 'Accept: application/xml' -o \"${CSAR}\" \"${PARTICLES_EXPORT_URL}/${NAMESPACE}/${SERVICE_TEMPLATE}/?yaml&csar\""
              archiveArtifacts artifacts: "${CSAR}", onlyIfSuccessful: true
            }
          }
        }
      }
    }
  }
  post {
    always {
      sh "docker-compose -f ${GMT_COMPOSE_FILE} rm -fsv"
    }
  }
}

