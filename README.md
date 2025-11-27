# 5G DU Demo

A lightweight Python project simulating a 5G Distributed Unit (DU), for demonstration purposes.  
This project demonstrates networking and containerization skills using docker, python & flask.
---

## Project Overview

- Simulates a 5G DU service with basic API endpoints.
- Provides real-time status of the DU, connected users, and system metrics.
- Containerized using Docker for easy deployment.
- Can be deployed locally or to free cloud platforms like Render.com or Fly.io.

---

## Features

-  Health check, confirms service is running.
-  Returns JSON data simulating DU metrics:
   - DU ID  
   - Cell Status  
   - Connected User Equipments (UEs)  
   - CPU and Memory Usage  

Example output:

```json
{
  "DU_ID": "DU001",
  "Cell_Status": "Active",
  "Connected_UEs": 5,
  "CPU_Usage": "15%",
  "Memory_Usage": "120MB"
}
