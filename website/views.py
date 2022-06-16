from crypt import methods
from distutils.log import error
from email.policy import EmailPolicy
from operator import contains
from flask import Blueprint, flash, render_template, request

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
                print("okay")
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
                modified_text_file.close()
                        
                        
                 
                

                
                
               # for line in text_file:
                    #if line != ">":   #To skip every line that starts with '>' in the text file
                       # x = x.replace(modify)  #To perform the replacement using the values of the created dictionary
                       # modified_text_file.write(x)
                    #else:
                       # modified_text_file.write(x)
                #modified_text_file.close()
                #file.close()
                    #for key in dictionary:
                        
                #flash('File formated successful Yes', category='success')
             
                
    data = request.form
    # print(modified_text_file.read())
    return render_template('analysis.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')
