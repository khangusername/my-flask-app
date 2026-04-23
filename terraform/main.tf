terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

provider "github" {
  token = var.github_token
  owner = var.github_owner
}

resource "github_repository" "flask_app" {
  name        = "my-flask-app"
  description = "Flask CI/CD demo with GitHub Actions, Docker, and Kubernetes"
  visibility  = "public"

  has_issues   = true
  has_projects = false
  has_wiki     = false

  delete_branch_on_merge = true
}

resource "github_branch_protection" "main" {
  repository_id = github_repository.flask_app.node_id
  pattern       = "main"

  required_status_checks {
    strict   = true
    contexts = ["build-and-test", "docker-build"]
  }

  required_pull_request_reviews {
    dismiss_stale_reviews = true
  }

  force_push_bypassers = []
}
