FROM public.ecr.aws/lambda/python:2.7

COPY app.py requirements.txt ./

RUN curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py

RUN {{cookiecutter.runtime}} get-pip.py

RUN rm -rf get-pip.y

RUN {{cookiecutter.runtime}} -m pip install -r requirements.txt -t .

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]
