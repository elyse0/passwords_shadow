# By Lester ^-^!

import ply.lex as lex
from ply.lex import TOKEN
import re

def getSaltHash(linuxPassword):

    # Lista de tokens
    tokens = (
        'SALT',  # Salt
        'HASH',  # Hash completo
        'EXTRA'  # Es lo que hay despues del $, alfanumerico
    )

    # Regular expression rules for simple tokens
    EXTRA = r'[A-Z,a-z,0-9,/,.]*'  # se uso cerradura de Kleene
    SALT = r'\$' + r'\d+' + r'\$' + EXTRA
    HASH = r'\$' + EXTRA

    # Definimos hash como token
    @TOKEN(SALT)
    def t_SALT(t):
        t.value = str(t.value)
        return t

    @TOKEN(HASH)
    def t_HASH(t):
        t.value = str(t.value[1:])
        return t

    t_ignore = ' \n'            # Ignorar el salto de linea

    def t_error(t):             # Saltar 1 caracter en caso de error
        t.lexer.skip(1)

    lexer = lex.lex()           # Creamos el lexer
    lexer.input(linuxPassword)  # Entrada de datos

    hashSalt = []

    while True:                 # Tokenize
        tok = lexer.token()
        if not tok:
            break  # CUANDO NO HAY MAS CARACTERES
        hashSalt.append(tok.value)

    return tuple(hashSalt)