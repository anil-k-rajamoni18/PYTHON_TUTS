FROM ubuntu:latest
RUN apt update 
RUN apt install python3-pip -y
RUN mkdir -p PythonProj
WORKDIR /app
COPY . .
CMD ["python3" ,"-m","flask","run","--host=0.0.0.0"]