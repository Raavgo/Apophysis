# 🐳 Docker

**Docker** is a platform for developing and running applications in isolated environments called containers. 

A container bundles all necessary components to execute an application, including source code, libraries, dependencies, runtime, and environment variables into a single, portable unit.
Docker leverages lightweight, container-based virtualization, allowing multiple applications to run simultaneously on the same system with minimal overhead, while ensuring process isolation.


# ⚙️ How does the Dockerfile work?
This Dockerfile sets up a slim Python 3.13 environment and uses Poetry for dependency management. 
Each step of the setup will be explained in detail below.

## 📦 Base Image
A lightweight Python 3.13 image is used to keep the image size small and fast.

## 🌐 Curl
The package list is updated retrieving the latest version from Debian repositories.
Docker installs Curl, a tool required to install Poetry.

## 📚 Poetry
Poetry, a dependency manager for Python, is downloaded and installed.
The `ENV` instruction updates the container's environment variables to ensure that the Poetry CLI is globally accessible within the container.

## 📁 Working Directory
The /app directory is set as the working directory within the container.
All subsequent instructions, such as copying files and installing dependencies, are executed relative to this path.

## 📝 Copy Project Files
This step copies the contents of the current directory on the host machine into the /app directory inside the container.
This guarantees that the container has access to all source code and resources required to run the application.

## 🐍 Python Version
Poetry is explicitly instructed to use Python 3.13 when creating and managing the virtual environment.
Using a controlled Python runtime guarantees that all dependencies are installed into the correct environment.

## 📦 Application Dependencies
This step installs all dependencies defined in the `pyproject.toml` file using Poetry.
The --no-root flag prevents Poetry from installing the application itself as a package, which is unnecessary when the application is executed inside the container.
