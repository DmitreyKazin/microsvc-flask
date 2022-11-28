# Micro Service with Flask

The purpose of this project is to practice microservices architecture, to enable rapid, frequent and reliable 
delivery of applications. The Flask application presents some network information generated with micro services. 

## Micro Services 
| SVC/Folder Name | Role | Port   
| :---:   | :---:   | :---: 
| ip-svc | fetches IPv4 using [ip_fy API](https://api.ipify.org?format=json) | 5001
| speedtest-svc | fetches speed test resoults using [speedtest-cli package](https://pypi.org/project/speedtest-cli/) | 5002
| dns-svc | Domain Information Groper request results sent to "example.com" using [networkcalc API](https://networkcalc.com/api/dns/lookup/example.com) | 5003
| backend-svc | Communicates with ip, speedtest and dns microservices and forwards responses to frontend service, served by gunicorn | 5000
| frontend-svc | Serves the web application using gunicorn production environment | 80
| nginx-svc | Acts as a reverse proxy to hanlde client requests | 1337

## Run The Application With Docker Compose

- **Run the application:**
```sh
# run the following command from the project directory
# you can use "-d" flag to run in de-attached mode
docker-compose up
```
- **Stop the application:**
```sh
# run the following command from the project directory
docker-compose down
```
