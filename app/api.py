import json
from typing import Any

import numpy as np
import pandas as pd
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from loguru import logger
from ssg_sea import __version__ as model_version
from ssg_sea.extract_skills import extract_skills

from app import __version__, schemas
from app.config import settings

api_router = APIRouter()


@api_router.get("/health", response_model=schemas.Health, status_code=200)
def health() -> dict:
    """
    Root Get
    """
    health_response = schemas.Health(
        name=settings.PROJECT_NAME, message="Welcome to the API",
        api_version=__version__, model_version=model_version
    )

    return health_response.dict()


@api_router.post("/extract", response_model=schemas.Extraction, status_code=200)
async def extract(input_data: schemas.SEAInputSchema) -> Any:
    """
    Make skills extractions with the SEA Algorithm
    """

    input_text = str(jsonable_encoder(input_data.text))

    logger.info(f"Performing extractions on inputs: {input_text}")
    results = extract_skills(text=input_text)

    logger.info(f"Extraction results: {results.get('extractions')}")

    return results
