from pydantic import BaseModel


class PreviewMaskSchema(BaseModel):
    rules: dict
