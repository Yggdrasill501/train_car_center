import os


class Process:
    """"""

    def __init__(self,
                 dir: str):
        """Initialize

        :param str dir: dircetory with data
        """
        self.dir = dir
        self.images: list = []
        self.labels: list = []

    def load(self):
        """Load images and their x and y coordinate"""

        files = sorted(os.listdir(dir))
        for file in files:
            
    def get_jpeg(file):
        """ """
        if file.endswith(".jpeg")

