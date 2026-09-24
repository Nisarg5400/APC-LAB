# 14. Media base class, play() overridden

class Media:
    def play(self):
        pass


class Audio(Media):
    def play(self):
        print("Playing audio track")


class Video(Media):
    def play(self):
        print("Playing video")


class Podcast(Media):
    def play(self):
        print("Playing podcast episode")


media_items = [Audio(), Video(), Podcast()]
for m in media_items:
    m.play()
