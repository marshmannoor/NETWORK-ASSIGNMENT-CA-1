Network Systems and Administration
Automated Container Deployment in the Cloud
-------------------------------------------

Group 4 - Dublin Business School
MS Cyber Security April 2026-2027

Muhammad Arshman Noor (20096163)
Khawaja Abdul Moiz (20089410)
Hammad Malik (20073974)

-----------------------------------------
WHAT IS THIS PROJECT?
-----------------------------------------

This project is an assignment for our networking subject.
In this assignment we had to deploy a web application on cloud server using
automation tools. We used Terraform to create the server on AWS, Docker to
run our app in a container, and GitHub Action to build and push Docker Image.

The app is a simple Flask Web page that shows our group details
You can see it live at: http://34.245.80.51

--------------------------------------------
TOOLS WE USED
--------------------------------------------

Terraform		: to create AWS server
Docker			: to containerized our Flask App
Docker Hub		: to store our Docker Image
GitHub Actions		: to automatically push and build the image
AWS EC2			: the cloud server where our app runs
Python + Flask		: the web application


---------------------------------------------
FILES IN THIS REPOSITORY
---------------------------------------------

main.tf
  This is the Terraform file. It tells AWS what server to create.
  It sets up an EC2 instance, opens ports 22 and 80, and installs
  Docker automatically when the server starts for the first time.

Dockerfile
  This tells Docker how to build our app into a container image.
  It uses Python 3.11, installs Flask, copies our app code,
  and starts the Flask server on port 80.

app.py
  This is the actual web application. It is a simple Flask app
  that shows our group name, module code, and member details
  when you visit the server IP in a browser.

requirements.txt
  Just one line: flask
  This tells pip what Python packages to install.

.github/workflows/deploy.yml
  This is the GitHub Actions pipeline file. Every time we push
  code to the main branch, it automatically builds our Docker
  image and pushes it to Docker Hub. Takes about 23 seconds.

.gitignore
  This tells Git to ignore the .terraform folder, terraform.tfstate,
  and other sensitive files so they dont get uploaded to GitHub.


---------------------------------------------------
HOW TO RUN THIS PROJECT FROM SCRATCH
---------------------------------------------------

Step 1 - Set up AWS
  - Create a free AWS account at aws.amazon.com/free
  - Go to IAM, create a user, and download the access keys
  - Install AWS CLI from aws.amazon.com/cli
  - Run: aws configure
  - Enter your Access Key, Secret Key, region (eu-west-1), format (json)

Step 2 - Set up Terraform
  - Download Terraform from developer.hashicorp.com/terraform/install
  - Extract the zip and add terraform.exe to your system PATH
  - Test it with: terraform --version

Step 3 - Generate SSH key
  - Run: ssh-keygen -t rsa -b 2048
  - Press Enter for all prompts
  - This creates id_rsa and id_rsa.pub in your .ssh folder

Step 4 - Create the AWS server
  - Open the project folder in terminal
  - Run: terraform init
  - Run: terraform apply
  - Type yes when asked
  - Copy the server IP address from the output

Step 5 - Install Docker Desktop
  - Download from docker.com/products/docker-desktop
  - Install and wait for "Engine running" at the bottom

Step 6 - Build and test the app locally
  - Run: docker build -t my-web-app .
  - Run: docker run -p 80:80 my-web-app
  - Open browser and go to http://localhost:80
  - Press Ctrl+C to stop

Step 7 - Push image to Docker Hub
  - Create account at hub.docker.com
  - Run: docker login -u YOUR_USERNAME
  - Run: docker tag my-web-app YOUR_USERNAME/my-web-app:latest
  - Run: docker push YOUR_USERNAME/my-web-app:latest

Step 8 - Set up GitHub Actions
  - Create a GitHub repo and push all files
  - Go to Settings > Secrets > Actions
  - Add these secrets:
      DOCKERHUB_USERNAME = your docker hub username
      DOCKERHUB_TOKEN    = your docker hub access token
  - Push any change to main branch to trigger the pipeline
  - Check the Actions tab on GitHub to see it run

Step 9 - Run the container on the server
  - Go to AWS console > EC2 > your instance > Connect
  - Click EC2 Instance Connect tab > Connect
  - In the browser terminal run:
      sudo apt-get install docker.io -y
      sudo docker pull YOUR_USERNAME/my-web-app:latest
      sudo docker run -d --name web-app -p 80:80 --restart always YOUR_USERNAME/my-web-app:latest

Step 10 - Check it works
  - Open your browser
  - Go to http://YOUR_SERVER_IP
  - You should see your web app live!


---------------------------------------------------
HOW TO UPDATE THE APP LATER
---------------------------------------------------

1. Edit app.py in VS Code and save
2. Run: docker build -t my-web-app .
3. Run: docker tag my-web-app YOUR_USERNAME/my-web-app:latest
4. Run: docker push YOUR_USERNAME/my-web-app:latest
5. On the server via EC2 Instance Connect:
     sudo docker stop web-app
     sudo docker rm web-app
     sudo docker pull YOUR_USERNAME/my-web-app:latest
     sudo docker run -d --name web-app -p 80:80 --restart always YOUR_USERNAME/my-web-app:latest
6. Push your code to GitHub too:
     git add .
     git commit -m "update app"
     git push


---------------------------------------------------
PROBLEMS I RAN INTO AND HOW WE FIXED THEM
---------------------------------------------------

Problem 1: Ansible doesnt work on Windows
  We planned to use Ansible but it does not run on Windows natively.
  Fix: We used Terraform user_data instead to install Docker on the server.

Problem 2: GitHub rejected our push because of a large file
  The .terraform folder had a 685MB file which is too big for GitHub.
  Fix: We used git filter-repo to remove it from history and added
  .terraform to our .gitignore file.

Problem 3: SSH kept saying Permission denied
  The SSH key on AWS didnt match our local key.
  Fix: We generated a new SSH key and recreated the server with terraform.

Problem 4: Docker Hub login kept failing
  We were using the wrong Docker Hub username.
  Fix: We logged into hub.docker.com and checked our exact username,
  then updated the GitHub secret with the correct one.

Problem 5: GitHub Actions pipeline SSH deploy step failed
  The pipeline could not SSH into the server to update the container.
  Fix: We removed the SSH deploy step from the pipeline for now.
  We update the container manually via EC2 Instance Connect instead.


---------------------------------------------------
IMPORTANT SECURITY NOTES
---------------------------------------------------

- Never put your AWS keys in any file that goes on GitHub
- Always add .terraform/ and terraform.tfstate to .gitignore
- Use Docker Hub access tokens, not your actual password
- Use GitHub Secrets to store any passwords or tokens in pipelines


---------------------------------------------------
REFERENCES
---------------------------------------------------

HashiCorp (2024) Terraform Docs - https://developer.hashicorp.com/terraform/docs
Docker Inc. (2024) Docker Docs - https://docs.docker.com
GitHub (2024) GitHub Actions Docs - https://docs.github.com/en/actions
AWS (2024) EC2 Docs - https://docs.aws.amazon.com/ec2
Red Hat (2024) Ansible Docs - https://docs.ansible.com







