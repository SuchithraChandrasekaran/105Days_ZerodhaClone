Jenkins CI/CD Pipeline for a Python Project Using Docker
-------------------

Objective
-------------------

The goal was to configure a Jenkins CI/CD pipeline to automate the build and execution of a Python project within a Docker container.

Key Steps
-------------------

Folder Structure:

  Workspace: Pipeline05

  Subfolder for the project: Day_5

  Files in Day_5:

    * Dockerfile

    * Python script: SimulateBuySell.py

    * Dockerfile:

Configured the Dockerfile to build an image that compiles and runs the Python script.

Jenkins Pipeline:
-------------------

  1.  Configured a Jenkins pipeline script to:

  2. Pull the repository.

  3. Build the Docker image.

  4. Run the Python script in a container.

Challenges Faced and Resolutions
-------------------

  1. File Not Found Errors:

      Issue: Python script SimulateBuySell.py was not found during execution.

      Resolution: Ensured the WORKDIR in the Dockerfile matched the script's location and all files were copied correctly.

  2. Invalid Docker Image Tag:

      Issue: Docker image tag contained uppercase letters.

      Resolution: Updated the tag to lowercase (pipeline05:latest).

  3. Docker Command Not Found:

      Issue: Jenkins could not locate the Docker CLI.

      Resolution: Added C:\Program Files\Docker\Docker\resources\bin to the Jenkins environment PATH under Manage Jenkins > Global Tool Configuration.

  4. Jenkins Shell Command Errors:

      Issue: Jenkins could not execute shell commands on Windows.

      Resolution: Configured the Jenkins pipeline to use the appropriate shell environment by specifying the PATH.

  5. Plugin Requirements:

      Issue: Missing plugins for Python, Java, and Docker.

      Resolution: Installed the following plugins via Manage Jenkins > Plugins:

          Python: Enabled Python integration.

          Java: Ensured compatibility for Java-based builds.

          Docker Pipeline: Integrated Docker commands into the Jenkins pipeline.

  6. Configured the shell environment within Jenkins.

      Shell Environment Setup:

        Configured sh commands in the pipeline to execute correctly.

        Updated the PATH environment variable in Jenkins to include:

            C:\WINDOWS\SYSTEM32

            C:\Program Files\Docker\Docker\resources\bin

Final Outcome
-------------------

  > Successfully configured a Jenkins pipeline to:

  > Pull a Python project from GitHub.

  > Build and run the project inside a Docker container.

  > This setup automated the entire process and ensured a streamlined CI/CD workflow.
