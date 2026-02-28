FROM jenkins/jenkins:lts-jdk17

USER root

RUN apt-get update && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*

# Install kubectl
RUN curl -LO "https://dl.k8s.io/release/v1.29.0/bin/linux/amd64/kubectl" \
    && install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl \
    && rm kubectl

# Install Kaniko
RUN curl -Lo /usr/local/bin/executor \
    https://github.com/GoogleContainerTools/kaniko/releases/latest/download/executor-linux-amd64 \
    && chmod +x /usr/local/bin/executor

RUN curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

USER jenkins

