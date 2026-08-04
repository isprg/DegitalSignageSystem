from flask import Flask, jsonify, render_template, request

try:
    from app.lib.load_video import load_videos
except ImportError:
    from lib.load_video import load_videos

app = Flask(__name__)

video_path = "static/videos/white.mp4"  # Default video path


@app.route("/")
def index():
    global video_path  # Declare video_path as global to modify it
    video_name = request.args.get("video")
    if video_name:
        video_path = f"static/videos/{video_name}"  # Update the video path based on the query parameter
    videos = load_videos()  # Load videos from the 'videos' directory
    return render_template("index.html", videos=videos, video_path=video_path)


@app.route("/view")
def view():
    return render_template("view.html")


@app.route("/video")
def video():
    return jsonify({"video_path": video_path})


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
