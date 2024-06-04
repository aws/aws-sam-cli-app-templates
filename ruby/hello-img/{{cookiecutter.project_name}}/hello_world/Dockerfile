# building phase
#
FROM public.ecr.aws/sam/build-ruby{{ cookiecutter.options[cookiecutter.runtime].version }} as build-image

ARG SCRATCH_DIR=/var/task/build

ENV GEM_HOME=${SCRATCH_DIR}

COPY app.rb Gemfile ./
RUN bundle install
RUN cp -r ${GEM_HOME}/* .
RUN rm -r ${GEM_HOME}

# runtime emulation phase
#
FROM public.ecr.aws/lambda/ruby:{{ cookiecutter.options[cookiecutter.runtime].version }}

ENV GEM_HOME=${LAMBDA_TASK_ROOT}

COPY --from=build-image /var/task/ ./

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]
