# 9. Abstract class CloudStorage with upload_file(), download_file(), delete_file()

from abc import ABC, abstractmethod

class CloudStorage(ABC):
    @abstractmethod
    def upload_file(self, filename):
        pass

    @abstractmethod
    def download_file(self, filename):
        pass

    @abstractmethod
    def delete_file(self, filename):
        pass


class GoogleDriveStorage(CloudStorage):
    def upload_file(self, filename):
        print(f"Uploading {filename} to Google Drive")

    def download_file(self, filename):
        print(f"Downloading {filename} from Google Drive")

    def delete_file(self, filename):
        print(f"Deleting {filename} from Google Drive")


class DropboxStorage(CloudStorage):
    def upload_file(self, filename):
        print(f"Uploading {filename} to Dropbox")

    def download_file(self, filename):
        print(f"Downloading {filename} from Dropbox")

    def delete_file(self, filename):
        print(f"Deleting {filename} from Dropbox")


services = [GoogleDriveStorage(), DropboxStorage()]
for s in services:
    s.upload_file("report.pdf")
    s.download_file("report.pdf")
    s.delete_file("report.pdf")
