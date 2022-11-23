FROM public.ecr.aws/amazonlinux/amazonlinux:2 as build-image
RUN yum install -y golang
WORKDIR /src
COPY go.mod go.sum main.go ./
RUN go build -o lambda-handler
FROM public.ecr.aws/amazonlinux/amazonlinux:2
COPY --from=build-image /src/lambda-handler /usr/local/bin
ENTRYPOINT lambda-handler
