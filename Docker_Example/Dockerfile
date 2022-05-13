FROM ubuntu:latest
RUN apt update 
RUN apt install python3-pip -y
WORKDIR /app
#RUN mkdir -p PythonProj
COPY . .
RUN pip3 install -r requirements.txt
CMD ["python3" ,"./app.py","--host=0.0.0.0"]