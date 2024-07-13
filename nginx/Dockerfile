FROM tiangolo/nginx-rtmp

# Instalar nano, nmap, ifconfig, net-tools y openssh-server
RUN apt-get update && \
    apt-get install -y nano nmap net-tools openssh-server && \
    rm -rf /var/lib/apt/lists/*

# Configurar SSH
RUN mkdir /var/run/sshd && \
    echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config && \
    echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config && \
    echo 'root:password' | chpasswd

# Exponer el puerto SSH
EXPOSE 22

# Iniciar SSH en el contenedor
CMD ["/usr/sbin/sshd", "-D"]

