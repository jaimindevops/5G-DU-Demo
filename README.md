5G DU Demo

This repository contains a lightweight demo application simulating a 5G Distributed Unit (DU)** environment.It is built with Python (Flask) and containerized using Docker.  
The project is intended to showcase hands-on experience with cloud-native deployment, Docker, and network-oriented applications for job applications.

---
 Features

- Simple Python Flask application representing 5G DU interactions.
- Dockerized for easy deployment.
- Can run locally or in any cloud environment (e.g., Azure, AWS, GCP).
- Exposes HTTP endpoint on port `8080`.

---

Tech Stack

- **Python 3.11**  
- **Flask 2.3.2**  
- **Docker**  

---

Getting Started

 Prerequisites

 - Docker installed (or Colima on macOS).  
 - Basic knowledge of command line.

Build & Run Locally

```bash
# Clone the repo
git clone https://github.com/jaimindevops/5G-DU-Demo.git
cd 5G-DU-Demo

# Build Docker image
docker build -t du-demo .

# Run the container
docker run -p 8080:8080 du-demo
````

 Access the app in your browser: `http://localhost:8080`

---

Pull from Docker Hub
 The image is available on Docker Hub:

```bash
docker pull jaimin180692/du-demo:latest
docker run -p 8080:8080 jaimin180692/du-demo
```

---

 Project Structure

```
5G-DU-Demo/
├── app.py           # Python Flask app simulating 5G DU
├── Dockerfile       # Container instructions
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
```

---

##  Demo Screenshot

(screenshot of app running locally or the Docker container in terminal)
<img width="932" height="34" alt="image" src="https://github.com/user-attachments/assets/a77ba00e-3b65-4bdc-b152-bbf2b61b2995" />

---

## 🔗 References

* [Flask Documentation](https://flask.palletsprojects.com/)
* [Docker Documentation](https://docs.docker.com/)

---

Next Steps

* Add unit tests for 5G DU simulation endpoints.
* Extend demo to simulate real-time 5G data flows.
* Deploy on Azure/AWS/GCP for cloud-native demonstration.

---
