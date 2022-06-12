from threading import Thread
import time

from app.models.domain.file import(
    File,
    FileData
)
from app.core.mkv2mp4 import mkv2mp4

class watcher(Thread):
        def __init__ (self, session, output_path):
            Thread.__init__(self)
            self.session = session
            self.output_path = output_path
        def run(self):
            while True:
                temp_data = File.find_by_id_status(self.session, 1)
                if temp_data:
                    for item in temp_data:
                        File.update(session=self.session, id=item.id, id_status=2)
                        inst_mkv2mp4 = mkv2mp4(item.original_path, self.output_path)
                        inst_mkv2mp4.create_cmd()
                        inst_mkv2mp4.run()
                        for out in inst_mkv2mp4.outs:
                            FileData.add(item.id, '1080p', 'xx', out)
                        File.update(session=self.session, id=item.id, id_status=3)
                time.sleep(5)