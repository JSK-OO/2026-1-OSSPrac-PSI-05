# 이미지명
FROM python:3

# python 컨테이너에서 사용되는 경로
WORKDIR /usr/src/app

# 현재 local 경로에 있는 디렉토리를 컨테이너 내부로 copy함
COPY . .

# Flask 구동을 위해 필요한 패키지 설치
# (requirements.txt가 있다면 RUN pip install -r requirements.txt 사용 권장)
RUN pip install flask

# python ./team.py가 실행됨 (백엔드 파일명에 맞춤)
CMD [ "python3", "team.py" ]