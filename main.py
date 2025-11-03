from abc import ABC, abstractmethod

# --- 1. CLASSES DE CONTEÚDO (HERANÇA E ENCAPSULAMENTO) ---

class Mensagem(ABC):
    """Classe base abstrata para todos os tipos de mensagem."""
    def __init__(self, conteudo):
        # Encapsulamento: Usa um atributo privado (convenção com _)
        self._conteudo = conteudo

    @abstractmethod
    def get_formato(self):
        """Método abstrato para retornar o formato da mensagem."""
        pass

    def get_conteudo(self):
        """Método público para acessar o conteúdo."""
        return self._conteudo

class MensagemTexto(Mensagem):
    """Mensagem simples de texto."""
    def get_formato(self):
        # Polimorfismo: Implementação específica para MensagemTexto
        return "Texto"

class MensagemVideo(Mensagem):
    """Mensagem de vídeo (URL ou path)."""
    def get_formato(self):
        # Polimorfismo: Implementação específica para MensagemVideo
        return "Vídeo"

class MensagemFoto(Mensagem):
    """Mensagem de foto/imagem."""
    def get_formato(self):
        return "Foto"

class MensagemArquivo(Mensagem):
    """Mensagem com um arquivo anexo."""
    def get_formato(self):
        return "Arquivo"


# --- 2. CLASSES DE CANAIS (HERANÇA E POLIMORFISMO) ---

class Canal(ABC):
    """Classe base abstrata para todos os canais de comunicação."""
    def __init__(self, nome_canal):
        self.nome_canal = nome_canal
        
    @abstractmethod
    def enviar_mensagem(self, mensagem: Mensagem, destinatario: str):
        """Método abstrato para enviar a mensagem."""
        pass

class WhatsApp(Canal):
    """Implementação para o canal WhatsApp."""
    def __init__(self):
        # Herança: Chama o construtor da classe base
        super().__init__("WhatsApp")

    def enviar_mensagem(self, mensagem: Mensagem, destinatario: str):
        # Polimorfismo: Lógica de envio específica para WhatsApp
        formato = mensagem.get_formato()
        conteudo = mensagem.get_conteudo()
        
        # Simulação da API de envio
        print(f"--- 📞 Enviando para {self.nome_canal} ({destinatario}) ---")
        print(f"  Formato: {formato}")
        print(f"  Conteúdo: '{conteudo[:20]}...'")
        print(f"  Status: ✅ Mensagem {formato} enviada com sucesso!")

class Telegram(Canal):
    """Implementação para o canal Telegram."""
    def __init__(self):
        super().__init__("Telegram")

    def enviar_mensagem(self, mensagem: Mensagem, destinatario: str):
        # Polimorfismo: Lógica de envio específica para Telegram
        formato = mensagem.get_formato()
        conteudo = mensagem.get_conteudo()
        
        print(f"--- 💬 Enviando para {self.nome_canal} ({destinatario}) ---")
        print(f"  Formato: {formato}")
        print(f"  Conteúdo: '{conteudo[:20]}...'")
        # Exemplo de tratamento específico: Telegram pode ter limite de tamanho
        if formato == "Vídeo" and len(conteudo) > 1000:
             print("  ⚠️ Atenção: Vídeo grande, pode levar mais tempo.")
        print(f"  Status: ✅ Mensagem {formato} despachada.")

# Você faria o mesmo para Facebook e Instagram...
class Facebook(Canal):
    def __init__(self):
        super().__init__("Facebook Messenger")

    def enviar_mensagem(self, mensagem: Mensagem, destinatario: str):
        # Lógica específica do Facebook
        formato = mensagem.get_formato()
        conteudo = mensagem.get_conteudo()
        print(f"--- 👍 Enviando para {self.nome_canal} ({destinatario}) ---")
        print(f"  Formato: {formato}")
        print(f"  Conteúdo: '{conteudo[:20]}...'")
        print(f"  Status: ✅ Publicado no Messenger.")

class Instagram(Canal):
    def __init__(self):
        super().__init__("Instagram Direct")

    def enviar_mensagem(self, mensagem: Mensagem, destinatario: str):
        # Lógica específica do Instagram
        formato = mensagem.get_formato()
        conteudo = mensagem.get_conteudo()
        print(f"--- 📸 Enviando para {self.nome_canal} ({destinatario}) ---")
        print(f"  Formato: {formato}")
        print(f"  Conteúdo: '{conteudo[:20]}...'")
        print(f"  Status: ✅ Enviado por Direct Message.")


# --- 3. CLASSE GERENCIADORA (ENCAPSULAMENTO) ---

class GerenciadorDeMensagens:
    """
    Classe que encapsula a lógica de seleção de canais e roteamento.
    """
    def __init__(self):
        # Encapsulamento: O gerenciador contém instâncias dos canais
        self._canais = {
            "whatsapp": WhatsApp(),
            "telegram": Telegram(),
            "facebook": Facebook(),
            "instagram": Instagram(),
        }

    def enviar(self, canal_nome: str, mensagem: Mensagem, destinatario: str):
        """
        Método público para enviar uma mensagem a um canal específico.
        """
        canal_nome = canal_nome.lower()
        if canal_nome not in self._canais:
            raise ValueError(f"Canal '{canal_nome}' não suportado.")
            
        canal = self._canais[canal_nome]
        
        # O gerenciador não se preocupa com o TIPO da mensagem, 
        # apenas a passa para o canal, que faz a chamada polimórfica.
        canal.enviar_mensagem(mensagem, destinatario)


# --- 4. EXEMPLO DE USO ---

if __name__ == "__main__":
    
    # 1. Cria o gerenciador (Encapsulamento)
    gerenciador = GerenciadorDeMensagens()

    # 2. Cria diferentes tipos de mensagens (Herança)
    msg_texto = MensagemTexto("Olá! Esta é uma mensagem de texto simples.")
    msg_video = MensagemVideo("https://video.mp4")
    msg_foto = MensagemFoto("/path/to/image.jpg")
    msg_arquivo = MensagemArquivo("/path/to/document.pdf")
    
    destinatario_wa = "@client_wa"
    destinatario_tg = "@client_tg"
    destinatario_fb = "user_facebook_id"
    
    print("=========================================")
    print("  DEMONSTRAÇÃO DE POLIMORFISMO E ROTEAMENTO  ")
    print("=========================================\n")
    
    # 3. Envia a mesma mensagem de TEXTO para canais diferentes (Polimorfismo em ação)
    # A chamada `enviar_mensagem` é a mesma, mas a implementação é diferente.
    print("--- ENVIO DE TEXTO ---")
    gerenciador.enviar("whatsapp", msg_texto, destinatario_wa)
    gerenciador.enviar("telegram", msg_texto, destinatario_tg)
    
    print("\n--- ENVIO DE VÍDEO ---")
    # 4. Envia diferentes tipos de mensagem
    gerenciador.enviar("whatsapp", msg_video, destinatario_wa)
    gerenciador.enviar("facebook", msg_foto, destinatario_fb)
    gerenciador.enviar("instagram", msg_arquivo, "user_insta_handle")