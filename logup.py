import streamlit as st
import streamlit_authenticator as stauth
import datetime
import re
from deta import Deta

DETA_KEY = 'YOUR_DETA_KEY'

deta = Deta(DETA_KEY)

db = deta.Base('YOUR_DETA_BASE')

def insert_user(name, username, password):
    """
    Inserts Users into the DB
    :param name:
    :param username:
    :param password:
    :return User Upon successful Creation:
    """
    date_joined = str(datetime.datetime.now())

    return db.put({'key': name, 'username': username, 'password': password, 'date_joined': date_joined})

def fetch_users():
    """
    Fetch Users
    :return Dictionary of Users:
    """
    users = db.fetch()
    return users.items

def get_user_names():
    """
    Fetch User Names
    :return List of user names:
    """
    users = db.fetch()
    names = []
    for user in users.items:
        names.append(user['key'])
    return names

def get_usernames():
    """
    Fetch Usernames
    :return List of user usernames:
    """
    users = db.fetch()
    usernames = []
    for user in users.items:
        usernames.append(user['username']) 
    return usernames

def validate_username(username):
    """
    Checks Validity of userName
    :param username:
    :return True if username is valid else False:
    """
    pattern = "^[a-zA-Z0-9]*$"
    if re.match(pattern, username):
        return True
    return False

def validate_name(name):
    """
    Check Name Validity
    :param name:
    :return True if name is valid else False:
    """
    pattern = "^[A-Za-z\s'-]+$"

    if re.match(pattern, name):
        return True
    return False

def sign_up():
    with st.form(key='signup', clear_on_submit=True):
        st.subheader(':green[Sign Up]')
        name = st.text_input(':blue[Name]', placeholder='Enter Your Name')
        username = st.text_input(':blue[Username]', placeholder='Enter Your Username')
        password1 = st.text_input(':blue[Password]', placeholder='Enter Your Password', type='password')
        password2 = st.text_input(':blue[Confirm Password]', placeholder='Confirm Your Password', type='password')

        if name:
            if validate_name(name):
                if name not in get_user_names():
                    if validate_username(username):
                        if username not in get_usernames():
                            if len(username) >= 2:
                                if len(password1) >= 6:
                                    if password1 == password2:
                                        # Add User to DB
                                        hashed_password = stauth.Hasher([password2]).generate()
                                        insert_user(name, username, hashed_password[0])
                                        st.success('Account created successfully!!')
                                        st.balloons()
                                    else:
                                        st.warning('Passwords Do Not Match')
                                else:
                                    st.warning('Password is too Short')
                            else:
                                st.warning('Username Too short')
                        else:
                            st.warning('Username Already Exists')
                    else:
                        st.warning('Invalid Username')
                else:
                    st.warning('Name Already exists!!')
            else:
                st.warning('Invalid Name')

        btn1, bt2, btn3, btn4, btn5 = st.columns(5)

    with btn3:
         st.form_submit_button('Sign Up')
         pass
        
    
