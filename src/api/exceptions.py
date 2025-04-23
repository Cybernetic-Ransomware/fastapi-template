from fastapi import HTTPException


class EndpointUnimplementedException(HTTPException):
    def __init__(self, message: str= ""):
        super().__init__(status_code=501, detail=f"Endpoint not implemented: {message}")

class EndpointUnexpectedException(HTTPException):
    def __init__(self, message: str= ""):
        super().__init__(status_code=404, detail=f"Unexpected Endpoint Error: {message}")
