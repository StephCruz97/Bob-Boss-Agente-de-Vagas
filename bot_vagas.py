import asyncio
import os
from dotenv import load_dotenv
from serpapi import GoogleSearch
from telegram import Bot

load_dotenv()

# ==============================
# CONFIGURAÇÕES (LENDO DO .ENV)
# ==============================
# Use sempre os mesmos nomes que definiu aqui em cima!
API_KEY = os.getenv("SERPAPI_KEY")
BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")
MEU_ID = os.getenv("TELEGRAM_USER_ID")

KEYWORDS = ["engenheiro planejamento obras", "gestão de projetos construção", "engenheiro civil", "engenheiro de obras"]
LOCATION = "Sao Paulo, Brazil"

STRATEGIC = ["planejamento", "gestão", "indicadores", "cronograma", "ms project", "primavera"]
OPERATIONAL = ["execução", "campo", "canteiro", "mestre", "pedreiro"]

# ==============================
# FUNÇÃO DE ANÁLISE
# ==============================
def analisar_vaga(job):
    titulo = job.get("title", "").lower()
    desc = job.get("description", "").lower()
    texto = titulo + " " + desc
    
    pontos = sum(2 for p in STRATEGIC if p in texto)
    pontos -= sum(1 for p in OPERATIONAL if p in texto)
    
    apply_options = job.get("apply_options", [])
    if apply_options and isinstance(apply_options, list):
        link_direto = apply_options[0].get("link")
    else:
        link_direto = job.get("link")

    return {
        "titulo": job.get("title"),
        "empresa": job.get("company_name"),
        "score": pontos,
        "link": link_direto,
        "via": job.get("via", "Google Jobs")
    }

# ==============================
# BUSCA E ENVIO
# ==============================
async def main():
    print(f"--- INICIANDO BUSCA EM {LOCATION} ---")
    vagas_totais = []
    ids_processados = set()
    
    for kw in KEYWORDS:
        print(f"Buscando: {kw}")
        params = {
            "engine": "google_jobs",
            "q": kw,
            "location": LOCATION,
            "hl": "pt",
            "gl": "br",
            "chips": "date_posted:today", 
            "api_key": API_KEY  # Corrigido aqui
        }
        
        try:
            search = GoogleSearch(params)
            results = search.get_dict()
            
            if "jobs_results" in results:
                jobs = results["jobs_results"]
                for item in jobs:
                    job_id = item.get("job_id")
                    if job_id not in ids_processados:
                        vaga = analisar_vaga(item)
                        if vaga["score"] >= 2:
                            vagas_totais.append(vaga)
                        ids_processados.add(job_id)
        except Exception as e:
            print(f"Erro na busca: {e}")

    if vagas_totais:
        print(f"Enviando {len(vagas_totais)} vagas...")
        bot = Bot(token=BOT_TOKEN) # Corrigido aqui
        
        # O Telegram ID precisa ser enviado como chat_id
        await bot.send_message(chat_id=MEU_ID, text="🚀 *NOVAS VAGAS ENCONTRADAS*", parse_mode='Markdown')

        for v in vagas_totais:
            t_clean = v['titulo'].replace('*', '').replace('_', '')
            
            msg = (
                f"📌 *{t_clean}*\n"
                f"🏢 {v['empresa']} ({v['via']})\n"
                f"⭐ Score: {v['score']}\n\n"
                f"🔗 [ABRIR CANDIDATURA]({v['link']})"
            )
            try:
                await bot.send_message(chat_id=MEU_ID, text=msg, parse_mode='Markdown') # Corrigido aqui
                await asyncio.sleep(1.5) 
            except Exception as e:
                print(f"Erro ao enviar: {e}")
    else:
        print("Nenhuma vaga estratégica nova hoje.")

if __name__ == "__main__":
    asyncio.run(main())

