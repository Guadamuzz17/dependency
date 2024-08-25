pipeline {
    agent any

    parameters {
        string(name: 'BOM_FILE', defaultValue: 'target/bom.xml', description: 'Ruta al archivo BOM para el análisis de Dependency Track')
        string(name: 'PROJECT_ID', defaultValue: 'your-project-id', description: 'ID del proyecto en Dependency Track')
        string(name: 'REPORT_OUTPUT', defaultValue: 'informe_vulnerabilidades.pdf', description: 'Nombre del archivo de informe PDF generado por Pandoc')
    }

    stages {
        stage('Análisis de Vulnerabilidades con Dependency Track') {
            steps {
                dependencyTrackPublisher artifact: "${params.BOM_FILE}", projectId: "${params.PROJECT_ID}"
            }
        }

        stage('Generar Informe con Pandoc') {
            steps {
                sh """
                pandoc -o ${params.REPORT_OUTPUT} \
                       -f markdown \
                       --metadata title="Informe de Vulnerabilidades" \
                       --metadata author="Tu Nombre" \
                       resultados_vulnerabilidades.md
                """
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: "${params.REPORT_OUTPUT}", allowEmptyArchive: true
        }
    }
}
