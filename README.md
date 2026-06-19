# Cyber Resilience Automation Platform

Proyecto de automatización orientado a monitoreo, recuperación automática de servicios y gestión de infraestructura.

## Objetivo

Implementar un flujo de resiliencia donde un servicio pueda ser monitoreado continuamente y recuperado automáticamente ante fallos utilizando herramientas de automatización.

## Arquitectura
            +----------------+
            |   monitor.py   |
            | Python Script  |
            +-------+--------+
                    |
                    |
             Health Check API
                    |
          +---------+---------+
          |                   |
        OK                  FAIL
          |                   |
          |             Ansible Recovery
          |                   |
          |                   |
          +------------ Docker Restart
                               |
                               |
                        Flask API Service

## Tecnologías utilizadas

- Python
- Flask
- Docker
- Ansible
- Linux / WSL2
- Git
- Terraform (Infrastructure as Code)

## Componentes

### Flask API

Servicio web con endpoint de salud:

Respuesta:

```json
{
  "status": "running",
  "service": "automation-api",
  "timestamp": "date"
}

Docker

La API se ejecuta dentro de un contenedor:

Construcción:
docker build -t automation-api -f docker/Dockerfile .


Ejecución:
docker run -d -p 5000:5000 --name automation-api automation-api

Monitoring

Script encargado de verificar disponibilidad:

python3 automation/monitor.py

Realiza chequeos periódicos del servicio.
Self-Healing Automation

Ante una falla:

Detecta caída del servicio.
Ejecuta playbook Ansible.
Reinicia automáticamente el contenedor Docker.
Verifica recuperación.
Ansible

Playbook utilizado:

ansible/restart_service.yml

Ejecuta:

Gestión del contenedor Docker.
Recuperación automática del servicio.
Estructura del proyecto
cyber-resilience-project

├── app
│   ├── app.py
│   └── requirements.txt
│
├── automation
│   └── monitor.py
│
├── ansible
│   ├── inventory
│   └── restart_service.yml
│
├── docker
│   └── Dockerfile
│
├── terraform
│
└── docs
Ejemplo de recuperación

Simulación de falla:

docker stop automation-api

El monitor detecta:

Servicio caído

Ejecuta:

Ansible Playbook

Resultado:

Servicio funcionando
## Infrastructure as Code

Terraform is used to provision and manage the Docker container infrastructure.

Commands:

terraform init

terraform plan

terraform apply
## Infrastructure as Code

Terraform is used to provision and manage the Docker container infrastructure.

Commands:

terraform init

terraform plan

terraform apply
