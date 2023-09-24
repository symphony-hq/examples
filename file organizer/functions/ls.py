import os
from typing import Optional, TypedDict, List
import json
import sys
from pydantic import Field, BaseModel


class SymphonyRequest(BaseModel):
    directory: str = Field(
        description="Directory to list files from")


class SymphonyResponse(BaseModel):
    files: List[str] = Field(description="List of files by name")


def handler(request: SymphonyRequest) -> SymphonyResponse:
    """
    Get list of files in a directory.
    """
    files = os.listdir(
        '/Users/<username>/{directory}'.format(directory=request.directory))
    return SymphonyResponse(files=files)


if __name__ == "__main__":
    args = json.loads(sys.argv[1])
    request = SymphonyRequest(**args)
    response = handler(request)
    print(response.json())
