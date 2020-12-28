class FilePickerScreenState:
    def __init__(self):
        # Using list instead of dict to maintain order when navigating between pages
        self.file_time_pairs = []
        self.keyCount = 0

    def add_record(self):
        self.file_time_pairs.append(FileTimePair(self.keyCount))
        self.keyCount += 1

    def update_record(self, filepath, time, key):
        for pairing in self.file_time_pairs:
            if pairing.key == key:
                pairing.filepath = filepath
                pairing.time = time
                break

    def remove_record(self, key):
        for pairing in self.file_time_pairs:
            if(pairing.key == key):
                self.file_time_pairs.remove(pairing)

    def get_data_string_summary(self):
        return list(map(lambda x: [x.filepath, x.time], self.file_time_pairs))


class FileTimePair:
    def __init__(self, key):
        self.filepath = ""
        self.time = 0
        self.key = key
