from django.core.mail import send_mail
def sendMail(title, recipient):
    subject = "WeTenn "+title
    message = 'This is to confirm that the bokking process has of a court at weTenn has been started \n The following is are the informations: \n Name: testing name \n Court: Testing court \n Session: testing session \n Time: testing time \n Type: testing couple \n Phone: testing phone \n '
    recipient_list = [recipient]

    send_mail(subject, message, from_email, recipient_list)