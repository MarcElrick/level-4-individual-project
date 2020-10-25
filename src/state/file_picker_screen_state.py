class FilePickerScreenState:
    def __init__(self):
        # Using list instead of dict to maintain order when navigating between pages
        self.file_time_pairs = []

    def add_record(self, record):
        self.file_time_pairs.append(record)

    def update_record(self, record, index):
        self.file_time_pairs[index] = record

    def remove_record(self, index):
        del self.file_time_pairs[index]
