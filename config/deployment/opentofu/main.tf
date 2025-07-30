terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "2.20.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "gdpr_app" {
  name         = "gdpr-app:latest"
  build_context = "${path.module}/../../.."
}

resource "docker_container" "gdpr_app" {
  name  = "gdpr_app"
  image = docker_image.gdpr_app.name
  ports {
    internal = 8000
    external = 8000
  }
}
