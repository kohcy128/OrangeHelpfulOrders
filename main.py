from flask import Flask, request, render_template_string

app = Flask(__name__)

# 웹페이지 내용
HTML = '''
<h1>체스닷컴 리뷰 사이트</h1>
<form method="POST">
    체스닷컴 게임 URL 입력: <input type="text" name="url">
    <button type="submit">리뷰 시작</button>
</form>

{% if url %}
    <p>입력한 URL: {{ url }}</p>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    url = None
    if request.method == 'POST':
        url = request.form['url']
        # 나중에 여기에 자동화 코드를 연결할 거야
    return render_template_string(HTML, url=url)

app.run(host='0.0.0.0', port=3000)