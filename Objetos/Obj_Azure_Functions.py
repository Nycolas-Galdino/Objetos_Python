from azure.storage.blob import BlobServiceClient


class AzureFunctions(object):
    def __init__(self, connection_string, container_name):
        self.connection_string = connection_string
        self.container_name = container_name
        self.client = BlobServiceClient.from_connection_string(self.connection_string)

    def upload_file(self, file_path, file_name):
        blob_client = self.client.get_blob_client(self.container_name, file_name)
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data)

    def download_file(self, file_name):
        blob_client = self.client.get_blob_client(self.container_name, file_name)
        with open(file_name, "wb") as download_file:
            download_file.write(blob_client.download_blob().readall())

    def delete_file(self, file_name):
        blob_client = self.client.get_blob_client(self.container_name, file_name)
        blob_client.delete_blob()

    def list_containers(self):
        generator = self.client.list_containers()
        for container in generator:
            print(container.name)

    def list_files(self):
        generator = self.client.get_container_client(self.container_name).list_blobs()
        for blob in generator:
            print(blob.name)

    def list_files_by_prefix(self, prefix):
        generator = self.client.get_container_client(self.container_name).list_blobs(name_starts_with=prefix)
        for blob in generator:
            print(blob.name)

    def list_files_by_suffix(self, suffix):
        generator = self.client.get_container_client(self.container_name).list_blobs(name_starts_with=suffix)
        for blob in generator:
            print(blob.name)

    def create_path(self, path):
        self.client.get_container_client(self.container_name).create_container(path)