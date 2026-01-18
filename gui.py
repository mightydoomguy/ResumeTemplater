import customtkinter as ctk
import requests
import configparser
import threading
import datetime
Config = configparser.ConfigParser()
Config.read("config.ini")

filename = datetime.datetime.now()
class MyApp(ctk.CTk):
    def __init__(self):
        super(MyApp,self).__init__()
        self.title("HumanSeller")
        self.geometry("600x600")
        self.grid()
        self.widget()
        self.load_cfg()

    def send_request(self,prompt):
        headers = {
            "Authorization": f"Bearer {self.api_mistral}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "mistral-large-latest",  # или другая модель, которую ты используешь
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(self.api_url_mistral, headers=headers, json=data)
        return response.json()
    def load_cfg(self):

        self.api_mistral = Config["API"]["api_key_mistral"]
        self.api_url_mistral = Config["API"]["mistral_url"]

    def savedump(self,data):
        self.filedumpname = self.dump_filename_input.get()
        with open(f"{self.filedumpname}.md", "w", encoding="UTF-8") as file:
            file.write(data)
            file.close()
    def generate_file(self):
        self.prompt_job_name = self.job_name_input.get()
        self.prmopt_type_person = self.type_of_person_input.get()
        self.prompt_skills = self.skills_input.get()
        self.prompt_xp_work = self.xp_work_input.get()
        self.prompt_education = self.education_input.get()
        self.prompt_wishes_for_work = self.wishes_for_work_input.get()
        self.filename = self.dump_filename_input.get()

        prompt = (
            f"Я {self.prmopt_type_person} ищу подходящую для себя работу составь мне резюме исходя из следующих входных данных: "
            f"Навыки:{self.prompt_skills}; "
            f"Опыт работы: {self.prompt_xp_work}"
            f"Образование{self.prompt_education}"
            f"Пожелания к работе:{self.prompt_wishes_for_work}"
            f"Профессия для резюме:{self.prompt_job_name}")

        self.result = self.send_request(prompt)
        self.res_new = self.result['choices']
        self.msg = self.res_new[0]['message']
        self.savedump(self.msg['content'])

        #print(f"{self.prompt_job_name},{self.prmopt_type_person},{self.prompt_skills},{self.prompt_xp_work},{self.prompt_education},{self.prompt_wishes_for_work},{self.filename}")
    def thread_file(self):
        self.thread_for_file = threading.Thread(target=self.generate_file,daemon=True)
        self.thread_for_file.start()
    def widget(self):
        #-------------------------------------------------------------------------
        self.job_name_input = ctk.CTkEntry(self,placeholder_text="Enter your job",width=400)
        self.job_name_input.pack(padx=10,pady=20)
        #----------------------------------------------------------------------------
        self.type_of_person_input = ctk.CTkEntry(self, placeholder_text="Enter your type of person(for example: intp-t)",width=400)
        self.type_of_person_input.pack(padx=10, pady=20)
        #--------------------------------
        self.skills_input = ctk.CTkEntry(self, placeholder_text="Enter your skills",width=400)
        self.skills_input.pack(padx=10, pady=20)
        #----------------
        self.xp_work_input = ctk.CTkEntry(self, placeholder_text="Enter your work xp",width=400)
        self.xp_work_input.pack(padx=10, pady=20)
        #-----------------
        self.education_input = ctk.CTkEntry(self, placeholder_text="Enter your education",width=400)
        self.education_input.pack(padx=10, pady=20)
        #------------------
        self.wishes_for_work_input = ctk.CTkEntry(self, placeholder_text="Enter your wishes for work",width=400)
        self.wishes_for_work_input.pack(padx=10, pady=20)
        #-------------------------------------------
        self.dump_filename_input = ctk.CTkEntry(self, placeholder_text="Dump_filename", width=400)
        self.dump_filename_input.pack(padx=10, pady=20)

        self.button = ctk.CTkButton(self,text="Generate File",command=self.thread_file)
        self.button.pack(padx=10, pady=20)
if __name__ == '__main__':
    app = MyApp()
    app.mainloop()