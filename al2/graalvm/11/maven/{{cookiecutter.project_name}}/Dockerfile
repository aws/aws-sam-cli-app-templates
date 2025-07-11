{%- if cookiecutter.architectures.value|length == 1 and cookiecutter.architectures.value[0] == 'arm64' %}
FROM --platform=linux/arm64 public.ecr.aws/amazonlinux/amazonlinux:2
{%- else %}
FROM --platform=linux/amd64 public.ecr.aws/amazonlinux/amazonlinux:2
{%- endif %}

RUN yum -y update \
    && yum install -y unzip tar gzip bzip2-devel ed gcc gcc-c++ gcc-gfortran \
    less libcurl-devel openssl openssl-devel readline-devel xz-devel wget \
    zlib-devel glibc-static libcxx libcxx-devel llvm-toolset-7 zlib-static \
    && rm -rf /var/cache/yum

# Graal VM
ENV JAVA_VERSION java11
ENV GRAAL_VERSION 22.1.0
ENV GRAAL_FOLDERNAME graalvm-ce-${JAVA_VERSION}-${GRAAL_VERSION}
{%- if cookiecutter.architectures.value|length == 1 and cookiecutter.architectures.value[0] == 'arm64' %}
ENV GRAAL_FILENAME graalvm-ce-${JAVA_VERSION}-linux-aarch64-${GRAAL_VERSION}.tar.gz
{%- else %}
ENV GRAAL_FILENAME graalvm-ce-${JAVA_VERSION}-linux-amd64-${GRAAL_VERSION}.tar.gz
{%- endif %}
RUN curl -4 -L https://github.com/graalvm/graalvm-ce-builds/releases/download/vm-${GRAAL_VERSION}/${GRAAL_FILENAME} | tar -xvz
RUN mv $GRAAL_FOLDERNAME /usr/lib/graalvm
RUN rm -rf $GRAAL_FOLDERNAME

# Maven
ENV MVN_VERSION 3.9.10
ENV MVN_FOLDERNAME apache-maven-${MVN_VERSION}
ENV MVN_FILENAME apache-maven-${MVN_VERSION}-bin.tar.gz
RUN curl -4 -L https://dlcdn.apache.org/maven/maven-3/${MVN_VERSION}/binaries/${MVN_FILENAME} | tar -xvz
RUN mv $MVN_FOLDERNAME /usr/lib/maven
RUN rm -rf $MVN_FOLDERNAME

# AWS Lambda Builders
RUN cd /tmp \
    && wget https://www.python.org/ftp/python/3.9.17/Python-3.9.17.tgz \
    && tar xvf Python-3.9.17.tgz \
    && cd Python-3.9.17 \
    && ./configure --enable-optimizations \
    && make install

RUN python3 -m ensurepip
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install aws-lambda-builders

VOLUME /project
WORKDIR /project

RUN /usr/lib/graalvm/bin/gu install native-image
RUN ln -s /usr/lib/graalvm/bin/native-image /usr/bin/native-image
RUN ln -s /usr/lib/maven/bin/mvn /usr/bin/mvn

ENV JAVA_HOME /usr/lib/graalvm

ENTRYPOINT ["sh"]