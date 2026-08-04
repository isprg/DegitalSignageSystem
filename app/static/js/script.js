const video = document.getElementById('movie');

alert("画面をクリックして、動画を再生してください。");

/*
* 動画のパスを取得する関数
*/
function playVideo() {
    getMoviePath().then((videoPath) => {
        if (videoPath) {
            video.src = videoPath;
            video.load();
            video.play();
        } else {
            console.error('動画のパスを取得できませんでした。');
        }
    });
}

/*
* 動画のクリックイベントリスナーを追加
*/
video.addEventListener('click', () => {
    playVideo();
});

/*
* 動画の再生終了イベントリスナーを追加
*/
video.addEventListener('ended', () => {
    setTimeout(() => {
        playVideo();
    }, 1000);
});
