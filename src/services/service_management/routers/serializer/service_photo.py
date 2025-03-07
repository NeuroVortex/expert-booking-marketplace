from fastapi import UploadFile

from src.shared.contract.media.service_photo import ServicePhoto


class ToServiceProfile:
    def __rmatmul__(self, file: UploadFile) -> ServicePhoto:
        return ServicePhoto()