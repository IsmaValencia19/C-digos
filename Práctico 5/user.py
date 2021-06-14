from flask import session, redirect, sessions

def Login(usuario):
    session['Nombre'] = usuario.Nombre
    session['DNI'] = usuario.DNI

def Logout():
    session.pop('Nombre', None)
    session.pop('DNI', None)