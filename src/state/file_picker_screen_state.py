class FilePickerScreenState:
    def __init__(self):
        # Using list instead of dict to maintain order when navigating between pages
        self.file_time_pairs = []
        self.keyCount = 0

    def add_record(self, filepath=""):
        self.file_time_pairs.append(FileTimePair(self.keyCount, filepath))
        self.keyCount += 1

    def remove_record(self, key):
        for pairing in self.file_time_pairs:
            if(pairing.key == key):
                self.file_time_pairs.remove(pairing)

    def get_data_string_summary(self):
        return list(map(lambda x: [x.filepath, x.time], self.file_time_pairs))


class FileTimePair:
    def __init__(self, key, filepath):
        self.filepath = filepath
        self.time = 0
        self.key = key
