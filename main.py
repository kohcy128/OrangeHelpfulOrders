from flask import Flask, request, render_template_string
import review  # review.py를 가져온다

app = Flask(__name__)

HTML = '''
<h1>체스닷컴 리뷰 사이트</h1>
<form method="POST">
    체스닷컴 게임 URL 입력: <input type="text" name="url">
    <button type="submit">리뷰 시작</button>
</form>

{% if url %}
    <p>입력한 URL: {{ url }}</p>
    <p>리뷰 준비 완료!</p>
{% endif %}
'''


@app.route('/', methods=['GET', 'POST'])
def home():
    url = None
    if request.method == 'POST':
        url = request.form['url']
        print("입력된 URL:", url)
        # 로그인 확인 코드 추가
        review.run_login_test()
    return render_template_string(HTML, url=url)


app.run(host='0.0.0.0', port=3000)
