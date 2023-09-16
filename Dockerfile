From alpine:3.7

RUN apk update && \
    apk add python python3 && \
    pip3 install flask  && \
    mkdir -p /workspace

WORKDIR /workspace

COPY app.py /workspace
COPY requirements.txt /workspace
RUN pip3 install -r requirements.txt


CMD ["flask", "run",  "--host=0.0.0.0", "--port=5000" ]