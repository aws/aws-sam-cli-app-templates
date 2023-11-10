FROM public.ecr.aws/lambda/python:3.11

COPY requirements.txt ./

# temporarily install gcc so that scikit-learn can be built
RUN yum install gcc-c++ -y

RUN python3.11 -m pip install -r requirements.txt -t .

COPY model /opt/ml/model
COPY app.py ./

CMD ["app.lambda_handler"]
