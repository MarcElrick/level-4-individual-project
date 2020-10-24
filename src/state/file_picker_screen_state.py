class FilePickerScreenState:
    def __init__(self):
        # Using list instead of dict as so that order doesn't change when navigating between pages.
        self.file_time_pairs = []
        print("STATE INITIALISED")

    def update_record(self, record):
        self.file_time_pairs[record[2]] = record
        print(self.file_time_pairs)

    def remove_record(self, index):
        del self.file_time_pairs[index]
        # Update all changed indexes to preserve original index value upon deletion.
        for item in self.file_time_pairs[index:]:
            item[2] -= 1
