terraform {

  required_providers {

    docker = {

      source = "kreuzwerker/docker"

      version = "~> 3.0"

    }

  }

}


provider "docker" {}


resource "docker_image" "automation_api" {

  name = "automation-api"

}


resource "docker_container" "automation_api" {

  name = "automation-api-terraform"

  image = docker_image.automation_api.image_id


  ports {

    internal = 5000

    external = 5001

  }

}
