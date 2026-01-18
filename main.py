import requests
import cowsay
from pypdf import PdfWriter
from fpdf import FPDF
token = "aVEm8VfXkufDP6MhcUm4Evo4jZGITBpn"
# Замени на свой API-ключ
API_KEY = token
# URL API Mistral (замени на актуальный, если нужно)
API_URL = "https://api.mistral.ai/v1/chat/completions"

writer = PdfWriter("")
def send_request(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistral-large-latest",  # или другая модель, которую ты используешь
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=data)
    return response.json()
def savedump(data):
    with open(f"queryAnswer.md","a+",encoding="UTF-8") as file:
        file.write(data)
        file.close()


def savepdf(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('DejaVu', '', font_path, uni=True)
    pdf.set_font('DejaVu', '', 12)

    # Add your data to the PDF
    pdf.cell(200, 10, txt=str(data), ln=1, align='C')
    pdf.output("somepdf.pdf")
def main():
    my_favorite_wrk = input("Введите профессию для резюме:>>>>")
    type_of_person = input('Введите тип личности:>>>>')
    skills = input("Введите ваши навыки через запятую:>>>>")
    expirience_of_work = input("Введите ваш опыт работы:>>>>")
    education = input("Введите ваше образование:>>>>")
    wishes_for_work = input("Введите пожелания к работе:>>>>")

    # Пример использования
    prompt = (f"Я {type_of_person} ищу подходящую для себя работу составь мне резюме исходя из следующих входных данных: "
              f"Навыки:{skills}; "
              f"Опыт работы: {expirience_of_work}"
              f"Образование{education}"
              f"Пожелания к работе:{wishes_for_work}"
              f"Профессия для резюме:{my_favorite_wrk}")
    result = send_request(prompt)
    #dict_keys(['id', 'created', 'model', 'usage', 'object', 'choices'])
    res_new = result['choices']
    msg = res_new[0]['message']
    print(msg['content'])
    savedump(msg['content'])
    savepdf(msg['content'])
if __name__ == '__main__':
    cowsay.tux("Привет этот скрипт  сделан для того чтобы ты помочь выставить себя на продажу")
    main()




