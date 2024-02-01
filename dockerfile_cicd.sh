#!/bin/bash

# 이미지 이름 설정
IMAGE_NAME="my-java-app"

# Docker 이미지 빌드
echo "Building Docker image..."
docker build -t $IMAGE_NAME .

# 이전에 실행 중이던 같은 이름의 컨테이너가 있으면 중지하고 제거
echo "Stopping and removing existing container..."
docker stop $IMAGE_NAME
docker rm $IMAGE_NAME

# Docker 컨테이너 실행
echo "Running Docker container..."
docker run -d -p 8011:8080 --name $IMAGE_NAME $IMAGE_NAME