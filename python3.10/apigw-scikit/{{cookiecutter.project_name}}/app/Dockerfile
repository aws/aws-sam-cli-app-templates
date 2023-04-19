FROM public.ecr.aws/lambda/python:3.10

COPY app.py requirements.txt ./
COPY model /opt/ml/model

# temporarily install gcc so that scikit-learn can be built
RUN yum install gcc-c++ -y

RUN python3.10 -m pip install -r requirements.txt -t .

CMD ["app.lambda_handler"]
