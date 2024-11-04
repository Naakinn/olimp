from g4f.client import Client

class TextGenerator:
    def __init__(self):
        self.client = Client(); 

    def generate(self, name, location, hotel_type, amenities, tone, features, lang):
        prompt = f"""
        Ты — профессиональный копирайтер, специализирующийся на написании 
        описаний отелей. Твоя задача — создать привлекательное и информативное 
        описание отеля на основе следующих характеристик: Создай описание 
        отеля на основе следующих характеристик: Название отеля: {name}, 
        Местоположение: {location}, Тип отеля: {hotel_type}, Удобства: {amenities}, 
        Особенности: {features}, Стиль текста: {tone}, Язык ответа: {lang}. 
        """
        # Формируем начальный текст
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}], 
            max_tokens=500
        )

        # Получаем ответ от модели
        gpt_response = response.choices[0].message.content
        return gpt_response
