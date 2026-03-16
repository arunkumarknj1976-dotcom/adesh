from flask import Flask, render_template, request
import yt_dlp
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    video_info = None
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            try:
                ydl_opts = {'format': 'best', 'quiet': True}
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    video_info = {
                        'title': info.get('title'),
                        'thumbnail': info.get('thumbnail'),
                        'url': info.get('url')
                    }
            except:
                video_info = {'error': "Invalid Link!"}
    return render_template('index.html', video_info=video_info)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
