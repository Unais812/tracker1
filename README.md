This web application demonstrates docker orchestration with Docker and docker compose 🐳

it features 3 services:

- Flask → backend web framework
- Redis → database for storage and tracking visits
- Nginx → acts as the reverse proxy so web server can handle increased load

Each service runs in its own container and communicate on the same docker network 

# Step 1 - Flask app 📚
I started by creating a flask app (count.py) with 2 routes:

> / : This is the welcome page
> /count : This is the count page which displays the amount of times the web page has been visited 

<img width="670" height="422" alt="Screenshot 2025-09-24 at 22 48 17" src="https://github.com/user-attachments/assets/9c3db3bc-58da-498d-af2d-1661a316e8c6" />

# Step 2 - Dockerfile 🐳
I created a Dockerfile which explained to docker how to run the app:
- Use python as base image
- Set the working directory to /app
- Copied the app files in the current directory i was in
- Installed the dependencies
- Exposed port 5002
- Ran my flask app and python

<img width="289" height="342" alt="Screenshot 2025-09-24 at 22 51 08" src="https://github.com/user-attachments/assets/bffcbb23-f8a5-41bd-ab93-9337fa1f4941" />

# Step 3 - docker compose 📪
Created a docker-compose.yml file to run my multiple services on a shared network so they are able to communicate

<img width="289" height="342" alt="Screenshot 2025-09-24 at 22 51 08" src="https://github.com/user-attachments/assets/747491eb-03bf-44a3-8418-2554248f9256" />

# Step 4 - volumes 🚀
At this point i thought i had finished but,

Everytime the container stopped, the counter would restart. 

To prevent this i introduced docker volume inside the docker-compose.yml file for persistent data storage because, 

this stores data inside the container so,

redis doesnt need to access the host machine for visit count, it now has it stored in the container. (see image in step 3 for the volume)

# Step 5 - env variables 💨
I also decided to implement env variables in my flask app 

This allowed me to seamlessly change configurations without modifying the code, in my case this was port number and host: 

<img width="456" height="132" alt="Screenshot 2025-09-24 at 23 07 24" src="https://github.com/user-attachments/assets/6cc0f7c1-a259-4c09-8207-80eab51369d7" />

# Step 6 
Even though it wasnt needed, i added nginx as a load balancer

This meant that my app was now resilient and capable of handling increased load

## nginx.conf file: 
<img width="424" height="294" alt="Screenshot 2025-09-24 at 23 11 00" src="https://github.com/user-attachments/assets/83b52c42-5aa1-413c-b26e-f1a30afdc175" />

## nginx as a service in my docker-compose.yml file:
<img width="419" height="181" alt="Screenshot 2025-09-24 at 23 12 06" src="https://github.com/user-attachments/assets/a87ae2ba-f835-47d3-9f04-e202a0d8dbf7" />

# Step 7 - finishing touches ✨
To finally finish it off,

i customised my web application using HTML styles to polish it and make it look neat!!
