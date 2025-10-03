# Requeriment:
pip install pyjwt
pip install "passlib[bcrypt]"

# Documentação
https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/

# Mão na massa
Manipular tokens JWT
Importe os módulos instalados.
Crie uma chave secreta aleatória que será usada para assinar os tokens JWT.
Para gerar uma chave secreta aleatória segura, use o comando:

'openssl rand -hex 32'
    4f06dd728ac253ee98031d99984bfd60a5cfe4d23be3c2e61b86f1ac049b414a

E copie a saída para a variável SECRET_KEY (Não use o exemplo)
Crie uma variável ALGORITHM com o algoritmo usado para assinar o token JWT e defina-a como "HS256".
Crie uma variável para a expiração do token.
Defina um modelo Pydantic que será usado no ponto de extremidade do token para a resposta.
Crie uma função utilitária para gerar um novo token de acesso.

