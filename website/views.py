# from crypt import methods
# from distutils.log import error
# from email.policy import EmailPolicy
# from operator import contains
import os
from re import M
from flask import Blueprint, flash, redirect, render_template, request, send_file
from flask_mail import Mail, Message
from . import mail

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('home.html')

@views.route('/analysis', methods = ['GET', 'POST'])
def analysis():
    if request.method == 'POST':
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        email = request.form.get('email')
        e_coil = request.form.get('e_coil')
      #  modify =request.form.get('modify')
        if len(firstName)<2 :
            flash('First name must be greater one character...',category='error')
        elif len (lastName)<2 :
            flash('Last name must be greater one character...', category='error')
        elif len(email)<2 :
             flash('Invalid email address...', category='error')
        #elif 'txt' not in e_coil:
             #flash('Invalid file ...', category='error')
       # elif len(modify)<2:
            #flash('Invalid modiflier ...', category='error')
        else:
           #create the dictionary
            dictionary = { 'D' : '(Kunpo)' , 'A' : 'mnm' }
            #open the text file in read only mode
            if request.files:
                file = request.files['e_coil']
             
                text_file = file.readlines()
               
                  #To open a modified text file
                modified_text_file = open("modified_text_file.txt", "w")
                
                for line in text_file:
                    
                 mline = line.decode()
                 if mline[0] != ">":   #To skip every line that starts with '>' in the text file
                        for key in dictionary:
                            mline = mline.replace(key, dictionary[key])  #To perform the replacement using the values of the created dictionary
                            modified_text_file.write(mline)
                            # print(mline)
                        
                        else:
                            modified_text_file.write(mline)
                            # print(mline)
                # modifiedFile = modified_text_file.readlines()  
                # moddecode = modifiedFile.decode()
                         
                print(modified_text_file.readable())  
                # with app.open_resource("invoice.pdf") as fp:  
                #     msg.attach("invoice.pdf", "application/pdf", fp.read())  
                
                # msg = Message('Hello', sender = 'daramolaadekunle15@gmail.com', recipients = [email])
                # msg.body = "This is the email body"
                # msg.attach("modified_text_file.txt", "text/txt")
                # mail.send(msg)     
                modified_text_file.close()
                p = "modified_text_file.txt"
                print(p)
                # filename = os.path.join( 'E-COIL', 'modified_text_file.txt')
                # send_file(p, as_attachment=True)
                        
                # return redirect('/download') 
                return render_template('download.html')       
                # flash('File formated successful And Formated file sent to your email', category='success')
               
             
                
    # data = request.form
    
    return  render_template('analysis.html') 

@views.route('/contact')
def contact():
    return render_template('download.html')

@views.route('/download')
def download_file():
    p = "modified_text_file.txt"
    return render_template('download.html')
    # return send_file(p, as_attachment=True)
