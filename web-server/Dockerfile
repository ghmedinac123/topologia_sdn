FROM ubuntu:20.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Update package lists and install required packages
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:ondrej/php -y && \
    apt-get update && \
    apt-get install -y \
    apache2 \
    php7.4 \
    libapache2-mod-php7.4 \
    exim4 \
    dovecot-core \
    dovecot-imapd \
    dovecot-pop3d \
    roundcube-core \
    roundcube-mysql \
    roundcube-plugins \
    roundcube-plugins-extra \
    iproute2 \
    iputils-ping \
    nmap \
    net-tools \
    vim \
    nano \
    curl \
    wget \
    openssh-server \
    sudo && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Enable Apache mods
RUN a2enmod php7.4 && a2enmod rewrite

# Create a user and grant sudo privileges
RUN useradd -m -s /bin/bash dockeruser && \
    echo 'dockeruser:dockerpassword' | chpasswd && \
    usermod -aG sudo dockeruser

# Configure SSH
RUN mkdir /var/run/sshd && \
    echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config && \
    echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config && \
    echo 'dockeruser ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# Copy Roundcube configuration
COPY config.inc.php /etc/roundcube/config.inc.php

# Expose ports
EXPOSE 22 80 443

# Start services
CMD service apache2 start && \
    service exim4 start && \
    service dovecot start && \
    service ssh start && \
    bash

