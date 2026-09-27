class LocalStorage:
    def save(self, filename, content):
        print(f"Saved {filename} on this computer")


class CloudStorage:
    def save(self, filename, content):
        print(f"Saved {filename} to cloud storage")


def upload_report(storage, filename, content):
    storage.save(filename, content)


upload_report(LocalStorage(), "sales.csv", "...")
upload_report(CloudStorage(), "sales.csv", "...")