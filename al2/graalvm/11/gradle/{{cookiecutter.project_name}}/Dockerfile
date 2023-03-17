{%- if cookiecutter.architectures.value|length == 1 and cookiecutter.architectures.value[0] == 'arm64' %}
FROM --platform=linux/arm64 public.ecr.aws/amazonlinux/amazonlinux:2
{%- else %}
FROM --platform=linux/amd64 public.ecr.aws/amazonlinux/amazonlinux:2
{%- endif %}

RUN yum -y update \
    && yum install -y unzip tar gzip bzip2-devel ed gcc gcc-c++ gcc-gfortran \
    less libcurl-devel openssl openssl-devel readline-devel xz-devel \
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

# Gradle
ENV GRADLE_VERSION 7.3.1
ENV GRADLE_FOLDERNAME gradle-${GRADLE_VERSION}
ENV GRALE_FILENAME ${GRADLE_FOLDERNAME}-bin.zip
RUN curl -L https://services.gradle.org/distributions/${GRALE_FILENAME} > $GRALE_FILENAME
RUN unzip -o $GRALE_FILENAME
RUN mv $GRADLE_FOLDERNAME /usr/lib/gradle
RUN rm $GRALE_FILENAME
ENV PATH=$PATH:/usr/lib/gradle/bin

# AWS Lambda Builders
RUN amazon-linux-extras enable python3.8
RUN yum clean metadata && yum -y install python3.8
RUN curl -L get-pip.io | python3.8
RUN pip3 install aws-lambda-builders

VOLUME /project
WORKDIR /project

RUN /usr/lib/graalvm/bin/gu install native-image
RUN ln -s /usr/lib/graalvm/bin/native-image /usr/bin/native-image
RUN ln -s /usr/lib/maven/bin/mvn /usr/bin/mvn

ENV JAVA_HOME /usr/lib/graalvm

ENTRYPOINT ["sh"]
