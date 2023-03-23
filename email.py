import smtplib
import email.message as emessage

def enviar_email():
    # Criando corpo do email
    # Usamos <p> para cada inicio e fim parágrafo
    corpo_email = """
    <p>Seu texto aqui...<p>


    <p>Att,<p>


    <p>Seu nome...<p>
    """
    msg = emessage.Message()
    msg['Subject'] = "ASSUNTO DO SEU EMAIL"
    msg['From'] = 'SEU_EMAIL'
    msg['To'] = 'EMAIL_DESTINATÁRIO'
    """Para o password, vá até as configurações da sua conta no Google e busque por 'Senhas de app'.
    Em seguida, gere a senha e copie e cole na 'SUA_SENHA'.
    """
    password = 'SUA_SENHA' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


enviar_email()


