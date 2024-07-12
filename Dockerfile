FROM tiangolo/nginx-rtmp

# Instalar nano, nmap, ifconfig y net-tools
RUN apt-get update && \
    apt-get install -y nano nmap net-tools && \
    rm -rf /var/lib/apt/lists/*

