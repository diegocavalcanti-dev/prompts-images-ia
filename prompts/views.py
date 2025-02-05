import os
import openai
from dotenv import load_dotenv
from ninja import NinjaAPI
from django.shortcuts import render
from .models import Prompt, Category, Style

load_dotenv()  # Carregar variáveis do .env
openai.api_key = os.getenv("OPENAI_API_KEY")

api = NinjaAPI()

@api.get("/")
def home(request):
    return render(request, "index.html")

@api.get("/generate/")
def generate_prompt(request, category: str = "geral", style: str = "realista"):
    prompt_text = f"Crie um prompt para uma imagem no estilo {style} sobre {category}."
    
    # Usando a nova API com a chave `messages`
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Alterado para GPT-3.5
    messages=[
        {"role": "system", "content": "Você é um especialista em criação de prompts para IA de imagens."},
        {"role": "user", "content": prompt_text}
    ],
    max_tokens=50  # Limite de tokens conforme necessário
)
    
    generated_prompt = response["choices"][0]["message"]["content"].strip()  # Acesso à resposta no novo formato
    prompt = Prompt.objects.create(text=generated_prompt)
    
    return {"prompt": generated_prompt}

@api.get("/categories/")
def list_categories(request):
    return {"categories": list(Category.objects.values_list("name", flat=True))}

@api.get("/styles/")
def list_styles(request):
    return {"styles": list(Style.objects.values_list("name", flat=True))}
