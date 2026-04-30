condicao_simbolo = ["@", "#", "$", "%", "&", "*", "!", "?"]                         #Criar as variaveis condicionais
condicao_numero = list("0123456789")
condicao_maiuscula = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
condicao_minuscula = list("abcdefghijklmnopqrstuvwxyz")

#Usuario
print("Como podemos lhe chamar?")                                                   # Pergunta para iniciar a criação do usuário
while True:                                                                         # Laço de repetição do usuário  
    login = input("Crie seu usuário (mínimo 6 caracteres): ")                       # Criar o login

    if len(login) <= 6:                                                             # Estabelecer a condição que o login precisa ser maior ou igual a 6 caracteres 
        print("Usuário precisa ter no mínimo 6 caracteres")
    else:
        break                                                                       # Quando a condição for obedecida o login estará concluido


#Senha
print("\nSua senha deve conter\n\nUma letra maiuscula;\nUma letra minuscula;\nUm numero;\nUm Simbolo")          #Um print com as informações necessárias para se criar a senha
while True:
    senha = input("Crie sua senha: ")

    tem_simbolo = any(c in condicao_simbolo for c in senha)                         #Essas linhas verificam se os itens correspondidos estão presentes na senha
    tem_numero = any(c in condicao_numero for c in senha)
    tem_maiuscula = any(c in condicao_maiuscula for c in senha)
    tem_minuscula = any(c in condicao_minuscula for c in senha)

    if len(senha) < 8:
        print("A senha deve ter no mínimo 8 caracteres")

    elif not tem_simbolo:                                                           # Estabelecem as condições da senha
      print("A senha deve conter um símbolo")

    elif not tem_numero:
        print("A senha deve conter um número")

    elif not tem_maiuscula:
        print("A senha deve conter uma letra maiúscula")

    elif not tem_minuscula:
        print("A senha deve conter uma letra minúscula")

    else:
        print("Senha válida criada com sucesso!")
        break                                                                       # Quando a senha passa por todas as condições é validada


print("\nCadastro concluído!")                                                      #Mostra que o cadastro foi finalizado  e mostra no final seu usuário e senha respectivamente
print("Usuário:", login)
print("Senha:", senha)
