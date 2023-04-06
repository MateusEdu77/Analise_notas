def verificacao(nome, ano, sala, escola, estado, cidade):
    import os
    diretorio_aluno = f'Analise_de_Notas/alunos/{estado}/{cidade}/{escola}/{ano} ano/sala {sala}/{nome}'
    if not os.path.exists(diretorio_aluno):
        os.makedirs(diretorio_aluno)