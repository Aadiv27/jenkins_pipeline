FROM redhat/ubi8

RUN yum install python3 -y && pip3 install flask

WORKDIR /app

COPY aapp.py /app/

CMD ["python3", "aapp.py"]