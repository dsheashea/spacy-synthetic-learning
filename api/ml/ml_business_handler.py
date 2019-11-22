import json
from .ml_service import MlService


class MLBusinessHandler:
    def __init__(self):
        self.ml_service = MlService()

    def check_spacy(self, request):
        return self.ml_service.static_string()
