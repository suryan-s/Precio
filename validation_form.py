from pydantic import BaseModel


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

