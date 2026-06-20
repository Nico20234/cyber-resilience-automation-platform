import requests
import time
import subprocess
import logging


logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


URL = "http://localhost:5000/health"


def restart_service():

    logging.warning("Ejecutando recuperación con Ansible")

    subprocess.run(
        [
            "ansible-playbook",
            "-i",
            "ansible/inventory",
            "ansible/restart_service.yml"
        ]
    )


while True:

    try:

        response = requests.get(URL, timeout=5)


        if response.status_code == 200:

            print("Servicio funcionando")

            logging.info("Servicio funcionando")


        else:

            print("Servicio caído")

            logging.error("Health check falló")

            restart_service()



    except Exception as e:

        print("Servicio caído")

        logging.error(f"Error detectado: {e}")

        restart_service()



    time.sleep(10)
