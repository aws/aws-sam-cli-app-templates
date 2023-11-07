FROM public.ecr.aws/lambda/python:3.10

COPY requirements.txt ./

RUN {{cookiecutter.runtime}} -m pip install -r requirements.txt -t .

COPY app.py ./

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]
