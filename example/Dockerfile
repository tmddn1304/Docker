# 기본 이미지 설정
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# 현재 디렉토리의 파일들을 이미지의 작업 디렉토리로 복사
COPY . /app

# 필요한 파일 인스톨
RUN pip install --no-cache-dir -r requirements.txt

# 앱 실행
CMD ["python", "test.py"]