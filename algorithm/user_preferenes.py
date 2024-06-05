class UserPreferences:
    def __init__(self, hour, temperature, humidity, precipitation_probability, cloud_cover, visibility, wind_speed, uv_index, is_day):
        self.hour = hour
        self.temperature = temperature
        self.humidity = humidity
        self.precipitation_probability = precipitation_probability
        self.cloud_cover = cloud_cover
        self.visibility = visibility
        self.wind_speed = wind_speed
        self.uv_index = uv_index
        self.is_day = is_day

    def update_values(self, hour=None, temperature=None, humidity=None, precipitation_probability=None, cloud_cover=None, visibility=None, wind_speed=None, uv_index=None, is_day=None):
        if hour is not None:
            self.hour = hour
        if temperature is not None:
            self.temperature = temperature
        if humidity is not None:
            self.humidity = humidity
        if precipitation_probability is not None:
            self.precipitation_probability = precipitation_probability
        if cloud_cover is not None:
            self.cloud_cover = cloud_cover
        if visibility is not None:
            self.visibility = visibility
        if wind_speed is not None:
            self.wind_speed = wind_speed
        if uv_index is not None:
            self.uv_index = uv_index
        if is_day is not None:
            self.is_day = is_day
            
    def bind_attributes(self):
        return self.hour, self.temperature, self.humidity, self.precipitation_probability, self.cloud_cover, self.visibility, self.wind_speed, self.uv_index, self.is_day

data = UserPreferences(18, 15, 50, 0, 0, 5000, 0, 0, True)
