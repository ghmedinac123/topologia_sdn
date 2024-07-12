FROM mariadb:latest

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Update package lists and install required packages
RUN apt-get update && \
    apt-get install -y \
    nano \
    nmap \
    net-tools \
    iputils-ping \
    iproute2 \
    openssh-server && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Configure SSH
RUN mkdir /var/run/sshd && \
    echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config && \
    echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config

# Expose ports
EXPOSE 22 3306

# Start services
CMD service ssh start && mysqld

