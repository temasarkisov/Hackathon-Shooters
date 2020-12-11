FROM ubuntu

RUN apt update && apt install -y git
RUN apt install -y python3-pip
RUN git clone https://github.com/temasarkisov/Hackathon-Shooters.git
RUN pip3 install -r ./Hackathon-Shooters/requirements.txt

ENTRYPOINT ["python3 ./Hackathon-Shooters/src/backend/main.py"]
