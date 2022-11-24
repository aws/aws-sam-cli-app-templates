FROM public.ecr.aws/docker/library/golang:1.19 as build-image
WORKDIR /src
COPY go.mod go.sum main.go ./
RUN go build -o lambda-handler
FROM public.ecr.aws/amazonlinux/amazonlinux:2
COPY --from=build-image /src/lambda-handler /usr/local/bin
ENTRYPOINT lambda-handler
