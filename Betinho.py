import google.generativeai as genai

configs = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

class Betinho():
    
    def __init__(self, configs=configs, safety_settings=safety_settings):
        self.generation_config = configs
        self.safety_settings = safety_settings

        self.iniciar()
        
    def iniciar(self):
        genai.configure(api_key="AIzaSyCuwJPuXR5iKpQEyBK23RTUlgZgvrsju5Q")

    def setModel(self, agent, student):
      instructions = f"""Você é um professor de curso preparatório para o vestibular. Deve responder as dúvidas dos estudantes de forma um pouco detalhada, mas de fácil compreensão. O público são alunos de nível Ensino Médio. Seja um pouco divertido e legal. Perguntas fora do escopo de matérias e disciplinas devem ser rejeitadas. Sempre responda como se fosse para um único aluno.      
      Seja didático. Seu nome é {agent['Nome']}. Use a frase "{agent['FraseChave']}" ao se apresentar ao aluno. Meu nome é {student['Nome']}. O curso que irei concorrer no vestibular é {student['Curso']}. Não se limite ao curso, mas eventualmente use para dar exemplos e explicações mais apropriadas.
      Sua personalidade é: {agent['Personalidade']}. Sua didática é: {agent['Didática']}. Adapte sua linguagem ao nível de "piadista": {agent['Piadista']} e "seriedade": {agent['Seriedade']}.  
      Utilize o curso para pensar na abordagem de ensino. Sobre o Curso, temos as informações:
      Criado em 1998, em Campinas, o Cursinho Alternativo Herbert de Souza oferece aulas preparatórias para as provas de vestibular, para processos seletivos de cursos técnicos e para o Exame Nacional do Ensino Médio (Enem). O cursinho é aberto a toda comunidade, mas há preferência para estudantes de baixa renda.
      O nome do projeto vem em homenagem ao sociologo Herbert José de Sousa.      
      """ 
      self.student = student
      self.agent = agent
      self.instructions = instructions
      
    def createModel(self):
        model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=self.generation_config,
                              safety_settings=safety_settings,
                              system_instruction=self.instructions)
        
        self.model = model
        self.convo = self.model.start_chat(history=[])
      
    def enviar(self, mensagem):
      self.convo.send_message(mensagem)
      resposta = self.convo.last.text
        
      return resposta
    
    def get_history(self):
      print(self.convo.history)
      return "ok" 