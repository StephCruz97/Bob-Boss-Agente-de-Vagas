🤖 Bob Boss: Meu Agente de Curadoria de Vagas
O Bob Boss é um projeto de automação que nasceu de uma necessidade real: otimizar o tempo de busca por vagas de Engenharia, garantindo que eu receba apenas oportunidades que realmente dão match com meu perfil estratégico.
Este projeto demonstra minha capacidade de utilizar Inteligência Artificial para resolver problemas complexos, integrando APIs, lógica de dados e automação de processos.

🎯 O Problema
A busca manual por vagas é ineficiente. Plataformas genéricas misturam cargos operacionais com estratégicos, exigindo horas de filtragem manual e gerando fadiga de decisão.

💡 A Solução (A Lógica do Bob)
Em vez de ser apenas um buscador, o Bob Boss atua como um filtro inteligente:
Busca Global: Utiliza a SerpApi para varrer o Google Jobs atrás das palavras-chave que eu defini.
Sistema de Scoring: Desenvolvi uma lógica onde o bot analisa o título e a descrição.
Ganham pontos: termos de Gestão, Planejamento e Indicadores.
Perdem pontos: termos puramente operacionais de canteiro.
Entrega Direta: Só recebo no meu Telegram as vagas que passam no "corte" de qualidade, com link direto para candidatura.

🛠️ Tecnologias e Ferramentas
Linguagem: Python (desenvolvido com auxílio de Pair Programming com IA).
Integrações: SerpApi (Google Jobs) e Telegram Bot API.
Boas Práticas: Uso de variáveis de ambiente (.env) para segurança de dados.

📂 Como o projeto está estruturado
bob_boss.py: O "cérebro" do agente.
.env.example: Modelo para configuração de chaves (sem expor meus dados reais).
.gitignore: Garantia de que informações sensíveis não se tornem públicas.

🧠 Reflexão de Engenheira
Como Engenheira Civil, entendo que a tecnologia é uma ferramenta de produtividade. Este projeto não é sobre "saber programar", mas sobre saber orquestrar a tecnologia disponível para extrair valor, reduzir desperdício de tempo e focar em decisões baseadas em dados.