import os
from pymediainfo import MediaInfo
import subprocess

class mkv2mp4(object):
    def __init__(self, input, output_path):
        self.input = input
        self.output_path = output_path
        self.media_info = MediaInfo.parse(self.input)
        self.audio_tracks = self.media_info.audio_tracks
        self.subtitle_tracks = self.media_info.text_tracks
        self.cmds = []
        self.outs = []
    def create_cmd(self):
        a_count = 0
        for item in self.audio_tracks:
            out = f'{name}-{item.language}.mp4'
            name = os.path.join(self.output_path, self.input.split('/')[-1:][0].replace('mkv', ''))
            cmd = f'ffmpeg -i {self.input} -c:v copy -c:a aac -map 0:v:0 -map 0:a:{a_count} -movflags +faststart {name}-{item.language}.mp4'
            self.cmds.append(cmd)
            self.outs.append(out)
            a_count += 1
    #     s_count = 0
    #     for item in self.subtitle_tracks:
    #         name = os.path.join(self.output_path, self.input.split('/')[-1:][0].replace('mkv', ''))
    #         cmd = f'ffmpeg -i {self.input} -map 0:s:{s_count} {name}-{item.language}.srt'
    #         print(cmd)
    #         self.cmds.append(cmd)
    #         s_count += 1
    # def run(self):
        for item in self.cmds:
            p = subprocess.Popen(item, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            (output, err) = p.communicate()
            print(output)
            p_status = p.wait()
            print(f'terminou {item}')

