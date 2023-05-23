from pytube import YouTube


def download_audio(url):
    try:
        video = YouTube(url)
        audio_stream = video.streams.filter(only_audio=True).first()
        output_path = audio_stream.download()
        output_file = output_path.split('\\')[-1].split('.')[0] + '.mp3'
        audio_stream.download(output_path=output_file)
        print(f"O áudio foi baixado com sucesso: {output_file}")
    except Exception as e:
        print("Ocorreu um erro durante o download do áudio:", str(e))


# Adicione as urls de vídeos para baixar o áudio na lista abaixo
urls = []

for url in urls:
    download_audio(url)
