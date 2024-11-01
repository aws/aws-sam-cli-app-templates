FROM public.ecr.aws/lambda/python:3.13

COPY app.py requirements.txt ./
COPY model /opt/ml/model

RUN python3.13 -m pip install -r requirements.txt -t .

CMD ["app.lambda_handler"]
