output "repository_url" {
  description = "GitHub repository URL"
  value       = github_repository.flask_app.html_url
}

output "repository_clone_url" {
  description = "SSH clone URL"
  value       = github_repository.flask_app.ssh_clone_url
}
