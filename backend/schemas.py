from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    email: str


class Token(BaseModel):
    status: int
    access_token: str
    token_type: str
    message: str


class CreateProject(BaseModel):
    project_name: str
    project_description: str
    project_type: str


class WMSData(BaseModel):
    maxtempC: int
    mintempC: int
    uvIndex: int
    DewPointC: int
    FeelsLikeC: int
    HeatIndexC: int
    WindChillC: int
    WindGustKmph: int
    humidity: int
    precipMM: float
    pressure: int
    tempC: int
    visibility: int
    winddirDegree: int
    windspeedKmph: int
    location: str