#from pytube import Caption
#from pytube import CaptionQuery
#from pytube import Channel
#from pytube import Playlist
#from pytube import Search
#from pytube import Stream
#from pytube import StreamQuery
from pytube import YouTube


"""link do video para test"""
url = "https://www.youtube.com/watch?v=t2StFyl-n_Q&ab_channel=HashtagPrograma%C3%A7%C3%A3o"

"""recupera o video em formato de objeto"""
yt = YouTube(url)

# acessar o nome do video
#print(yt.title)

"""mostra o caminho para a foto miniatura do video"""
#print(yt.thumbnail_url)


"""Baixar video com itag 17"""
#caminho = "/home/alexsandre/Área de Trabalho/usando-pytube/videos/"
#yt.streams.get_by_itag(17).download(output_path=caminho)

"""Buscar audios do video"""
#audios = yt.streams.filter(type="audio")
#audios = yt.streams.filter(only_audio=True)
#for audio in audios:
#    print(audio)


"""Listar todos os streams"""
# for stream in yt.streams.filter(progressive=True):
#     print(stream)

l = yt.streams.filter(progressive=True).get_highest_resolution()   

# l eh do tipo Stream
print(f"baixando... {l.title}")
l.download("./videos/")
print("Processo de download finalizado.")
# print(l.__str__())

#yt.streams.get_by_itag("17").download("./videos/")

#progressive = "True": video esta com audio
#progressive = "False": video sem audio 
