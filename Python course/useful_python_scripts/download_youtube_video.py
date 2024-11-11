from pytubefix import YouTube
from pytubefix.cli import on_progress

# video_link = 'https://www.youtube.com/live/idFEKNPAMt8?si=cxWKnTNFmFtyrjZV'
# download_path = r'C:\Users\User\Downloads>'
# title = ''


def download_video(url, path):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        print(yt.title)
        ys = yt.streams.get_highest_resolution()
        ys.download(output_path=path)
    except Exception as e:
        print(f"An error occurred: {e}")


def main(video_link, download_path):
    download_video(url=video_link,
                   path=download_path)


if __name__ == '__main__':
    main(video_link='https://www.youtube.com/live/82kzy8iY7Mc?si=cN8O6xeD3dsJgjNA',
         download_path='C:\\Users\\User\\Downloads')





