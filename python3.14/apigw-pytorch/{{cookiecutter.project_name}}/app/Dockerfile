FROM public.ecr.aws/lambda/python:3.14

COPY app.py requirements.txt ./
COPY model /opt/ml/model

RUN python3.14 -m pip install -r requirements.txt -t .

CMD ["app.lambda_handler"]
