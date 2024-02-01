#!/bin/bash

# 현재 디렉토리의 docker-compose.yml 파일 사용
COMPOSE_FILE=./docker-compose.yml

# docker-compose 서비스 상태 확인
if [ $(docker-compose -f $COMPOSE_FILE ps -q | wc -l) -gt 0 ]; then
    echo "Stopping and removing existing Docker Compose services..."
    docker-compose -f $COMPOSE_FILE down
fi

# Docker Compose 서비스 시작
echo "Starting Docker Compose services..."
docker-compose -f $COMPOSE_FILE up -d