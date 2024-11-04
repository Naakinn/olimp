from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

class TextGenerator:
    def __init__(self):
        # Загрузка предобученной модели и токенизатора
        self.tokenizer = GPT2Tokenizer.from_pretrained('sberbank-ai/rugpt3small_based_on_gpt2')
        self.model = GPT2LMHeadModel.from_pretrained('sberbank-ai/rugpt3small_based_on_gpt2')
        self.model.eval()

    def generate(self, name, location, hotel_type, amenities, tone):
        # Формируем начальный текст
        prompt = f"{name} — это {hotel_type.lower()} в {location}."

        if amenities:
            prompt += f" В отеле доступны следующие удобства: {amenities.lower()}."

        if tone == "Дружелюбный":
            prompt += " Мы всегда рады новым гостям и сделаем все, чтобы ваше пребывание было комфортным!"
        elif tone == "Официальный":
            prompt += " Мы обеспечим вам максимальный комфорт и лучшее обслуживание."
        elif tone == "Маркетинговый":
            prompt += " Забронируйте сейчас и окунитесь в атмосферу роскоши и комфорта!"

        # Генерация текста с помощью модели
        inputs = self.tokenizer.encode(prompt, return_tensors='pt')
        with torch.no_grad():
            outputs = self.model.generate(
                inputs,
                max_length=200,
                num_return_sequences=1,
                no_repeat_ngram_size=2,
                do_sample=True,
                top_p=0.95,
                top_k=60
            )
        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        return generated_text