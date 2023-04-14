from django.core.exceptions import ValidationError
import os


class FileValidator:
    def __init__(self, byte_limit: int):
        self.byte_limit = byte_limit

    @staticmethod
    def check_local_file_exist(path: str) -> bool | str:
        if os.path.isfile(path):
            return False
        return path

    def check_file_size(self, file) -> ValidationError or None:
        if file.size > self.byte_limit * 1024 * 1024:
            raise ValidationError(f"Max size file {self.byte_limit}MB")
