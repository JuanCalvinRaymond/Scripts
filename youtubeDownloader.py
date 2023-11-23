from sys import argv
from pathlib import Path
from pytube import YouTube
from pytube import Playlist
from pytube import Channel

KotohaCoverPlaylist = 'https://www.youtube.com/watch?v=oK_AxMSxlkg&list=PLFPTffQioGfbVs1_nh6hkiKdds3jUI1Fs'
KotohaCollabPlaylist = 'https://www.youtube.com/watch?v=A7KgiPfb1q4&list=PLFPTffQioGfazEZ8Do8yqlSA-AIVIT4Eg'
HakoniwalilyPlaylist = 'https://www.youtube.com/watch?v=kmH0EPyPgkw&list=PLFPTffQioGfYFs7Az7h0PusfVyCPI6iVe'
HakoniwalilyMVPlaylist = 'https://www.youtube.com/watch?v=LAaqqTrqxPk&list=PLGejWpTS0U0Ix0pa3UZJE4LMWGm7IHcqs'
HakoniwaLilyCoverPlaylist = 'https://www.youtube.com/watch?v=BLihH3vfOUw&list=PLGejWpTS0U0JSoFeRk93wHOhGitwg6Tml'
TMPlaylist = 'https://www.youtube.com/watch?v=jJ2BcHvASn4&list=PLHT9gVuoyrhfjUB-22BPbjFsts7xtskP4'

downloadAudio = False
destinationFolder = ''
DEFAULTDOWNLOADPATH = Path.home() / 'Videos'

def main():
    if len(argv) > 1:
        if argv[1] == '-h':
            help()
            return
        youtube = YouTube(argv[1])
        for index in range(2, len(argv)):
            if argv[index].startswith('-'):
                if argv[index] == '-a':
                    downloadAudio = True
            else:
                destinationFolder = argv[index]

        if downloadAudio:
            if len(destinationFolder):
                youtube.streams.get_audio_only().download(destinationFolder)
            else:
                youtube.streams.get_audio_only().download(DEFAULTDOWNLOADPATH)
        else:
            if len(destinationFolder):
                youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(destinationFolder)
            else:
                youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    else:
        print('Please provide Youtube link! ex. youtubeDownloader.py https://www.youtube.com/watch?v=_GuOjXYl5ew')

def help():
    print("""----------Help----------
-a - Only Download Audio""")
    
if __name__ == "__main__":
    main()

# playlist = Playlist(HakoniwalilyMVPlaylist)
# print(f'Downloading: {playlist.title}')
# for video in playlist.videos:
#     print(video.title)
#     video.streams.get_audio_only().download('C:\\Users\\fanaz\\Videos\\Kotoha Collab Playlist')

# Channel is not working
# channel = Channel('https://www.youtube.com/c/capiccino')
# print(f'Downloading videos by: {channel.channel_name}')
# # print(f'Video Count: {channel.video_urls[0]}')
# for video in channel.videos:
#     print(video.title)


