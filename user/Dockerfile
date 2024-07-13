FROM consol/ubuntu-xfce-vnc:latest

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV USER=root
ENV PASSWORD=password

# Update and install necessary packages
USER root
RUN apt-get update && \
    apt-get install -y \
    net-tools \
    iproute2 \
    iputils-ping \
    supervisor \
    vim \
    wget \
    curl \
    git \
    python3 \
    nano \
    openssh-server \
    vlc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Configure SSH
RUN mkdir /var/run/sshd && \
    echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config && \
    echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config && \
    echo 'root:password' | chpasswd

# Set up a supervisor to manage SSH
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose ports
EXPOSE 22 5901 8080

# Start supervisor
CMD ["/usr/bin/supervisord"]

