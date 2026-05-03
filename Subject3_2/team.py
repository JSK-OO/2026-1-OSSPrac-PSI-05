from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 팀원 정보 데이터 (4명으로 수정됨)
team_members = [
    {
        "name": "김양우",
        "student_id": "20245678",
        "gender": "남성",
        "department": "컴퓨터공학과",
        "languages": "Python, C++, Java, MATLAB",
        "role": "백엔드 개발 및 서버 아키텍처 설계",
        "intro": "시스템 프로그래밍과 로우레벨 아키텍처에 관심이 많은 개발자입니다. 전체적인 시스템 구조 설계와 안정적인 서버 구축을 담당하고 있습니다.",
        "photo": "member1.png"
    },
    {
        "name": "박현준",
        "student_id": "20245678",
        "gender": "남성",
        "department": "소프트웨어학과",
        "languages": "JavaScript, HTML/CSS, React",
        "role": "프론트엔드 개발 및 UI/UX",
        "intro": "직관적이고 사용자 친화적인 웹 인터페이스를 고민하는 개발자입니다. 프로젝트의 얼굴이 되는 웹 페이지의 디자인과 클라이언트 로직을 책임집니다.",
        "photo": "member2.png"
    },
    {
        "name": "임여민",
        "student_id": "20249012",
        "gender": "여성",
        "department": "인공지능학과",
        "languages": "Python, SQL, R",
        "role": "데이터베이스 설계 및 데이터 처리",
        "intro": "데이터의 흐름을 분석하고 구조화하는 것을 좋아합니다. 프로젝트 내 DB 스키마 설계 및 효율적인 데이터 파이프라인 구축을 맡고 있습니다.",
        "photo": "member3.png"
    },
    {
        "name": "김준성",
        "student_id": "20243456",
        "gender": "남성",
        "department": "컴퓨터공학과",
        "languages": "C, Linux/Bash, Docker",
        "role": "인프라 구축 및 배포 관리",
        "intro": "안정적인 서비스 운영과 자동화에 관심이 많습니다. 완성된 프로젝트가 Nginx와 연동되어 원활하게 배포될 수 있도록 서버 환경을 구성합니다.",
        "photo": "member4.png"
    }
]

@app.route('/')
def index():
    return render_template('index.html', members=team_members)

@app.route('/input')
def input_page():
    return render_template('input.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/result', methods=['POST'])
def result_page():
    new_member = {
        "name": request.form.get('name'),
        "student_id": request.form.get('student_id'),
        "gender": request.form.get('gender'),
        "department": request.form.get('department'),
        "languages": request.form.get('languages'),
        "role": request.form.get('role'),
        "intro": request.form.get('intro'),
        "photo": "" 
    }
    
    team_members.append(new_member)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)