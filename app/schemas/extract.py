from pydantic import BaseModel


class SEAInputSchema(BaseModel):
    text: str

    class Config:
        schema_extra = {
            "example": {
                "text": "Managing your Food and Beverage Supply Chain Learn the most detail-oriented, "
                        "scientific processes that go into running a restaurant and the challenges with "
                        "keeping food costs controlled.In this course, you'll learn to optimize your "
                        "operations profits by effectively managing your selection, procurement, "
                        "receiving, storage, and inventory management processes.",
            }
        }


class Extraction(BaseModel):
    extractions: dict
