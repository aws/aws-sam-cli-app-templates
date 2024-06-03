FROM public.ecr.aws/lambda/ruby:{{ cookiecutter.options[cookiecutter.runtime].version }}

COPY app.rb Gemfile ./

ENV GEM_HOME=${LAMBDA_TASK_ROOT}

# Install dev tools so that `bigdecimal` (a dep of httparty) can be installed
RUN yum install gcc make -y
RUN bundle install
# Remove the dev tools
RUN yum remove gcc make -y

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]
