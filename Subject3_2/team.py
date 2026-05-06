import os
import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# JSON 파일 경로 설정
DATA_FILE = 'team_data.json'

# 데이터를 파일에서 읽어오는 함수
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# 데이터를 파일에 저장하는 함수
def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

@app.route('/')
def index():
    # 파일에서 최신 데이터를 불러와서 화면에 전달
    team_members = load_data()
    return render_template('index.html', members=team_members)

@app.route('/member/<int:member_id>')
def member_detail(member_id):
    team_members = load_data()
    member = next((m for m in team_members if m['id'] == member_id), None)
    if member:
        return render_template('member.html', member=member)
    return "팀원을 찾을 수 없습니다.", 404

@app.route('/input', methods=['GET', 'POST'])
def input_page():
    if request.method == 'POST':
        # (기존에 작성하신 예비 로직 유지)
        return redirect(url_for('index'))
    return render_template('input.html')

@app.route('/result', methods=['POST'])
def result_page():
    team_members = load_data()
    
    # 새로운 팀원의 ID 자동 생성 (가장 마지막 ID + 1)
    new_id = max([m.get('id', 0) for m in team_members]) + 1 if team_members else 1
    
    # 폼에서 전달받은 언어 리스트 (아이콘 호환을 위해 소문자로 변환)
    raw_languages = request.form.getlist('languages')
    languages_lower = [lang.lower() for lang in raw_languages]

    # 새로 입력된 데이터와, 폼에 없는 누락된 필수 정보(기본값)를 함께 구성
    new_member = {
        "id": new_id,
        "name": request.form.get('name'),
        "student_id": request.form.get('student_number'), 
        "gender": request.form.get('gender'),
        "department": request.form.get('major'),
        "languages": languages_lower,
        
        # 폼에 없는 데이터들은 임시 기본값으로 채워 넣음 (화면 깨짐 방지)
        "role": "신규 합류 팀원",
        "intro": "새로 합류하게 된 팀원입니다. 잘 부탁드립니다!",
        "contribution": "아직 기여 내용이 기록되지 않았습니다.",
        "photo": "https://randomuser.me/api/portraits/lego/1.jpg", # 레고 얼굴 사진
        "github": "#",
        "email": "new_member@example.com",
        "portfolio": "#"
    }
    
    # 1. 리스트에 추가
    team_members.append(new_member)
    
    # 2. 변경된 전체 리스트를 다시 JSON 파일에 덮어쓰기 (영구 저장!)
    save_data(team_members)
    
    return render_template('result.html', member=new_member)

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

# 팀원 정보 수정 페이지 라우트
@app.route('/edit/<int:member_id>', methods=['GET', 'POST'])
def edit_page(member_id):
    team_members = load_data()
    
    # 수정할 팀원이 리스트의 몇 번째(index)에 있는지 찾기
    member_index = next((index for (index, m) in enumerate(team_members) if m['id'] == member_id), None)
    
    if member_index is None:
        return "팀원을 찾을 수 없습니다.", 404
        
    if request.method == 'POST':
        # 폼에서 넘어온 기존 데이터들 덮어쓰기
        team_members[member_index]['name'] = request.form.get('name')
        team_members[member_index]['student_id'] = request.form.get('student_number')
        team_members[member_index]['gender'] = request.form.get('gender')
        team_members[member_index]['department'] = request.form.get('major')
        
        raw_languages = request.form.getlist('languages')
        team_members[member_index]['languages'] = [lang.lower() for lang in raw_languages]
        
        # 👇 새롭게 추가된 부분: 자기소개와 사진 URL도 덮어쓰기 👇
        team_members[member_index]['intro'] = request.form.get('intro')
        team_members[member_index]['photo'] = request.form.get('photo')
        
        # JSON 파일에 덮어쓰기(저장) 후 이동
        save_data(team_members)
        return redirect(url_for('member_detail', member_id=member_id))
        
    return render_template('edit.html', member=team_members[member_index])

# --- (기존 코드 생략) ---

# 팀원 삭제 라우트 추가
@app.route('/delete/<int:member_id>', methods=['POST'])
def delete_member(member_id):
    team_members = load_data()
    
    # 삭제하려는 ID를 제외한 나머지 팀원들만 골라서 새로운 리스트를 만듭니다.
    updated_members = [m for m in team_members if m['id'] != member_id]
    
    # 길이가 달라졌다면 (삭제가 정상적으로 진행되었다면) 파일에 덮어씁니다.
    if len(team_members) != len(updated_members):
        save_data(updated_members)
        
    # 삭제가 완료되면 메인 화면으로 돌아갑니다.
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)