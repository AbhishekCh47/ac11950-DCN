# Dockerfile for Authoritative Server (AS)
FROM python:3.9-slim

WORKDIR /usr/src/app

COPY . .

# Expose port 53533 for the DNS server (UDP)
EXPOSE 53533/udp

# Run the Authoritative Server script
CMD ["python", "authoritative_server.py"]
