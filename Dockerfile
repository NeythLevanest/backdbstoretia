FROM ubuntu:latest
RUN echo Updating existing packages, installing and upgrading python and pip.
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install --upgrade pip
RUN echo Copying the TIA Store AppSD service into a service directory.
COPY ./dbstoretia /TIAStoreAppSDService
WORKDIR /TIAStoreAppSDService
RUN echo Installing Python packages listed in requirements.txt
RUN pip install -r requirements.txt
RUN echo Starting python and starting the DJANGO REST API service...
ENTRYPOINT ["python"]
#CMD ["mythicalMysfitsService.py"]