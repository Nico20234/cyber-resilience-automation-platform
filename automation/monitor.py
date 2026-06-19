import requests
import time
import subprocess


SERVICE_URL = "http://localhost:5000/health"
CONTAINER_NAME = "automation-api"


def restart_service():

    print("Reiniciando servicio...")

    subprocess.run(
        ["docker", "start", CONTAINER_NAME]
    )


def check_service():

    try:

        response = requests.get(
            SERVICE_URL,
            timeout=5
        )

        if response.status_code == 200:
            print("Servicio funcionando")

        else:
            print("Servicio con problemas")


    except Exception:

        print("Servicio caído")

        restart_service()



while True:

    check_service()

    time.sleep(10)
