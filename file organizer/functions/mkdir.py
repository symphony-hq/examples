import os
from typing import Optional, TypedDict, List
import json
import sys
from pydantic import Field, BaseModel


class SymphonyRequest(BaseModel):
    name: str = Field(description="Name of the folder to create")
    directory: str = Field(description="Directory to create the folder in")


class SymphonyResponse(BaseModel):
    pass


def handler(request: SymphonyRequest) -> SymphonyResponse:
    """
    Create a folder in the current directory
    """

    os.mkdir('/Users/<username>/{directory}/{name}'.format(
        directory=request.directory, name=request.name))

    return SymphonyResponse()


if __name__ == "__main__":
    args = json.loads(sys.argv[1])
    request = SymphonyRequest(**args)
    response = handler(request)
    print(response.json())
