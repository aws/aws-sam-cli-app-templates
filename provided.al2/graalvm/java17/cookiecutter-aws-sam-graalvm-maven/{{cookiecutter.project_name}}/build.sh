#!/bin/sh

set -e

docker build -t al2-graalvm .
sam build --use-container --build-image al2-graalvm