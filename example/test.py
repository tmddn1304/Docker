import socket

import requests
import os

def download_file(url, filename):
    # URL에서 파일을 다운로드하는 함수
    response = requests.get(url)
    
    # 요청이 성공적인지 확인
    if response.status_code == 200:
        # 파일 쓰기
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded '{filename}' from '{url}'")

        # 다운로드된 파일의 절대 경로 출력
        abs_path = os.path.abspath(filename)
        print(f"File saved to '{abs_path}'")
    else:
        print(f"Error downloading file from '{url}'")

# 사용 예시
url = "https://i.namu.wiki/i/qIuOCS3WWzBOS-qLXWP_onB3g5lsqGEAq6ZUwa0Ie-muLehPGC6DXlr0UvBWGunHCyw89qUD0g9uHwzOiU5rShaR7MNrkrMerxwIN6F9BAKBoVFMFT_C6jGLWComMKWI09gpUOx_080LC9VRmjKj6ox7oukMKUqw4VzFr9xKWMs.webp"
filename = "my_downloaded_image.webp"
download_file(url, filename)



hostname = socket.gethostname()
print(hostname)