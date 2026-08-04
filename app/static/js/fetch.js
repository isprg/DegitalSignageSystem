/*
* 動画のパスを取得する関数
*/
const getMoviePath = async () => {
    try {
        const response = await fetch('/video');
        if (!response.ok) {
            throw new Error('Failed to fetch video path');
        }
        const data = await response.json();
        console.log('Fetched video path:', data.video_path);
        return data.video_path;
    } catch (error) {
        console.error('Error fetching video path:', error);
        return null;
    }
};