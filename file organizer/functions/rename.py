import os
from typing import Optional, TypedDict, List
import json
import sys
from pydantic import Field, BaseModel


class SymphonyRequest(BaseModel):
    old_directory: str = Field(description="Old directory")
    new_directory: str = Field(description="New directory")


class SymphonyResponse(BaseModel):
    pass


def handler(request: SymphonyRequest) -> SymphonyResponse:
    """
    Rename file or directories
    """

    os.rename(
        "/Users/<username>/{directory}".format(
            directory=request.old_directory),
        "/Users/<username>/{directory}".format(directory=request.new_directory))

    return SymphonyResponse()


if __name__ == "__main__":
    args = json.loads(sys.argv[1])
    request = SymphonyRequest(**args)
    response = handler(request)
    print(response.json())
