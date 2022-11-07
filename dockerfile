FROM ubuntu:18.04
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install pyyaml
RUN ln -s /usr/bin/python3 /usr/bin/python
ADD config.yaml /config.yaml
ADD test.py /test.py
RUN chmod 777 /test.py
WORKDIR /
ENTRYPOINT ["./test.py"]
