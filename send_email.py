import os
import win32com.client

# Enviar correo atravéz de outlook
def main(project_address, MAIL_TO, MAIL_CC):
    # Crear instancia de Outlook
    outlook = win32com.client.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0) # 0 = MailItem

    # Leer el archivo HTML
    with open(os.path.join(project_address, 'index.html'), "r", encoding="utf-8") as f:
        html_body = f.read()

    # Guardar o usar el HTML final
    html_body = str(html_body)

    # Asunto
    mail.Subject = f'ALERTA: Detección de contrato cerca a finalizar'
    
    # Destinatarios principales
    mail.To = MAIL_TO

    # Con copia (CC)
    mail.CC = MAIL_CC

    # Cuerpo en HTML
    mail.HTMLBody = html_body

    # (Opcional) Agregar archivo adjunto
    # mail.Attachments.Add("C:\\ruta\\al\\archivo.pdf")

    # Enviar el correo
    mail.Send()