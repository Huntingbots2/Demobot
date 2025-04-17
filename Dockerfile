FROM python:3.8.5-slim-buster

WORKDIR /AsunaRobot/

# Install PostgreSQL development libraries
RUN apt-get update && apt-get install -y libpq-dev && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get upgrade -y
RUN apt-get -y install git
RUN python3 -m pip install -U pip
RUN apt-get install -y wget python3-pip curl bash neofetch ffmpeg software-properties-common
RUN apt-get install -y --no-install-recommends ffmpeg

COPY requirements.txt .

# Install Python dependencies
RUN pip3 install wheel
RUN pip3 install --no-cache-dir -U -r requirements.txt

COPY . .
CMD ["python3", "-m", "AsunaRobot"]
