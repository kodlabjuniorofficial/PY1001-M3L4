import json
import requests

class Assistant:
    def __init__(self, name):
        self.name = name
        self.filename = f"{self.name}.json"
        self.command_count = 0
        self.battery = 100 
        self.memory = [] 
        self.load_memory() 

    def search_info(self, topic):
        formatted_topic = topic.replace(" ", "_")
        url = f"https://tr.wikipedia.org/api/rest_v1/page/summary/{formatted_topic}"
        headers = {'User-Agent': 'BilgeBot/1.0'}
        
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                # Extract ve Görsel bilgisini çekiyoruz
                text = data.get("extract", "Özet bilgi bulunamadı.")
                img = data.get("thumbnail", {}).get("source", None)
                
                self.command_count += 1
                self.battery -= 5
                self.save_memory()
                
                return {"status": "ok", "topic": topic, "text": text, "image": img}
            else:
                return {"status": "error", "message": "Maalesef bu konuyu bulamadım. 🧐"}
        except:
            return {"status": "error", "message": "İnternet bağlantısında bir hata oluştu! 🌐"}

    def greet(self):
        if self.battery > 0:
            self.command_count += 1
            self.battery -= 5
            self.save_memory()
            return f"Merhaba! Ben {self.name}. İnternetten bilgi çekmek için /nedir [konu] yazabilirsin! 🤖"
        return "🪫 Enerjim bitti! Lütfen beni /sarj et."

    def charge(self):
        self.battery = 100
        self.save_memory()
        return "🔌 Şarj tamam! Bilgi araştırmaya hazırım. ⚡"

    def show_status(self):
        return f"📊 DURUM RAPORU\n🤖 İsim: {self.name}\n🔋 Pil: %{self.battery}\n📝 Notlar: {len(self.memory)}\n🔢 Komut: {self.command_count}"

    def set_name(self, new_name):
        self.name = new_name
        self.save_memory()
        return f"✅ Yeni adım: {self.name}"

    def add_note(self, note_text):
        self.memory.append(note_text)
        self.save_memory()
        return f"📝 Hafızaya alındı: {note_text}"

    def save_memory(self):
        data = {"battery": self.battery, "count": self.command_count, "memory": self.memory}
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)

    def load_memory(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.battery = data.get("battery", 100)
                self.command_count = data.get("count", 0)
                self.memory = data.get("memory", [])
        except FileNotFoundError: pass