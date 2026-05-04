from flask import Flask, render_template, request

app = Flask(__name__)

# 확장된 팀원 정보 데이터[cite: 1]
team_members = [
    {
        "id": 1,
        "name": "김양우",
        "student_id": "20245678",
        "gender": "남성",
        "department": "컴퓨터공학과",
        # Devicon 로고 클래스 매핑을 위해 영어 소문자/정확한 명칭 사용
        "languages": ["python", "cplusplus", "java", "matlab"],
        "role": "백엔드 개발 및 서버 아키텍처 설계",
        "intro": "시스템 프로그래밍과 로우레벨 아키텍처에 관심이 많은 개발자입니다. 전체적인 시스템 구조 설계와 안정적인 서버 구축을 담당하고 있습니다.",
        "contribution": "Flask 기반의 REST API 설계 및 구현, 데이터베이스 모델링, 로깅 및 예외 처리 시스템 구축",
        "photo": "https://randomuser.me/api/portraits/men/32.jpg", # 가상 인물 사진(남)
        "github": "https://github.com/kimyangwoo",
        "email": "yangwoo@example.com",
        "portfolio": "https://yangwoo.dev"
    },
    {
        "id": 2,
        "name": "박현준",
        "student_id": "20245678",
        "gender": "남성",
        "department": "소프트웨어학과",
        "languages": ["javascript", "html5", "react"],
        "role": "프론트엔드 개발 및 UI/UX",
        "intro": "직관적이고 사용자 친화적인 웹 인터페이스를 고민하는 개발자입니다. 프로젝트의 얼굴이 되는 웹 페이지의 디자인과 클라이언트 로직을 책임집니다.",
        "contribution": "Bootstrap을 활용한 반응형 UI/UX 디자인, 다크모드 및 애니메이션 구현, 컴포넌트 기반 아키텍처 설계",
        "photo": "https://randomuser.me/api/portraits/men/44.jpg", # 가상 인물 사진(남)
        "github": "https://github.com/parkhyunjun",
        "email": "hyunjun@example.com",
        "portfolio": "https://hyunjun.design"
    },
    {
        "id": 3,
        "name": "임여민",
        "student_id": "20249012",
        "gender": "여성",
        "department": "인공지능학과",
        "languages": ["python", "sqldeveloper", "r"],
        "role": "데이터베이스 설계 및 데이터 처리",
        "intro": "데이터의 흐름을 분석하고 구조화하는 것을 좋아합니다. 프로젝트 내 DB 스키마 설계 및 효율적인 데이터 파이프라인 구축을 맡고 있습니다.",
        "contribution": "RDB 스키마 정규화 및 최적화, 대용량 데이터 처리 파이프라인 설계, 데이터 시각화 컴포넌트 연동",
        "photo": "https://randomuser.me/api/portraits/women/68.jpg", # 가상 인물 사진(여)
        "github": "https://github.com/Yeomin-Yim",
        "email": "yeomin@example.com",
        "portfolio": "https://yeomin.data"
    },
    {
        "id": 4,
        "name": "김준성",
        "student_id": "20243456",
        "gender": "남성",
        "department": "컴퓨터공학과",
        "languages": ["c", "bash", "docker"],
        "role": "인프라 구축 및 배포 관리",
        "intro": "안정적인 서비스 운영과 자동화에 관심이 많습니다. 완성된 프로젝트가 Nginx와 연동되어 원활하게 배포될 수 있도록 서버 환경을 구성합니다.",
        "contribution": "Docker 기반의 컨테이너화, Nginx 리버스 프록시 설정, CI/CD 파이프라인 구축 및 무중단 배포 적용",
        "photo": "https://randomuser.me/api/portraits/men/75.jpg", # 가상 인물 사진(남)
        "github": "https://github.com/kimjunsung",
        "email": "junsung@example.com",
        "portfolio": "https://junsung.infra"
    }
]

@app.route('/')
def index():
    return render_template('index.html', members=team_members)

# 팀원 상세 페이지 라우트 추가
@app.route('/member/<int:member_id>')
def member_detail(member_id):
    # ID로 팀원 검색
    member = next((m for m in team_members if m['id'] == member_id), None)
    if member:
        return render_template('member.html', member=member)
    return "팀원을 찾을 수 없습니다.", 404

@app.route('/input')
def input_page():
    return render_template('input.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/result', methods=['POST'])
def result_page():
    # 입력만 받고 기존 리스트에 추가하지 않음 (고정 유지 목적)
    new_member = {
        "name": request.form.get('name'),
        "student_id": request.form.get('student_id'),
        "gender": request.form.get('gender'),
        "department": request.form.get('department'),
        "languages": request.form.get('languages'),
    }
    return render_template('result.html', member=new_member)

# contact.html을 렌더링하기 위한 라우트 추가
@app.route('/contact')
def contact_page():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
