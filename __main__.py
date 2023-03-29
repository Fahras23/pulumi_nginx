"""A Python Pulumi program"""

import pulumi
import pulumi_docker as docker

remoteInstance = docker.Provider(
    'remote'
    host: 'ssh://user@remote-host:22'
    )

nginxImage = docker.RemoteImage(
    'nginx',
    name="nginx:1.21.3-alpine"
)
nginxContainer = docker.Container(
    "nginx",
    image=nginxImage.repo_digest,
    ports=[docker.ContainerPortArgs(
    internal=80,
    external=8080
    )],
    )
