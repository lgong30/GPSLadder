import os
import re
class GPSLadder(object):
    """GPS Ladder"""

    def __init__(self, data_full_filename):
        self.ladder_data = []
        self.ladder_nodes = []
        self.width = 0
        self.height = 0
        with open(data_full_filename, "r") as fp:
            for line in fp:
                line = line.strip()
                if line.startswith("#") or (len(line) == 0):
                    # ignore comment lines and empty lines
                    continue
                else:
                    wh = re.split(r"\s+", line)
                    w = float(wh[0].strip())
                    h = float(wh[1].strip())
                    self.width += w
                    self.height += h
                    self.ladder_data.append((w, h))
        self._process_data()

    def _process_data(self):
        x = 0
        y = self.height

        for w, h in self.ladder_data:
            self.ladder_nodes.append({
                "x": x,
                "y": y
            })
            x += w
            self.ladder_nodes.append({
                "x": x,
                "y": y
            })
            y -= h
        self.ladder_nodes.append({
            "x": x,
            "y": y
        })

    def arrival_handler(self):
        """TODO"""
        pass

    def to_string(self):
        """TODO"""
        pass


