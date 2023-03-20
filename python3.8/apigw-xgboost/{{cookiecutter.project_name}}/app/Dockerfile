FROM public.ecr.aws/lambda/python:3.8

RUN yum install -y libgomp

COPY requirements.txt ./
RUN python3.8 -m pip install -r requirements.txt -t .

COPY app.py ./
COPY model /opt/ml/model

CMD ["app.lambda_handler"]
