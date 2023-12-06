group "default" {
    targets = ["my_repo_name"]
}

target "my_repo_name" {
    context = "./"
    dockerfile = Dockerfile
    platforms = ["linux/amd64", "linux/arm64"]
    tags = ["MYID.dkr.ecr.us-east-1.amazonaws.com/my_repo_name:latest"]
}
