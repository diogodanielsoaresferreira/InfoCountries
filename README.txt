O projeto foi desenvolvido no sistema operativo Windows 10 utilizando
a linguagem de programação Python (3.6.2) e a framework Django(1.11.5).

Para executar a aplicação são necessários os seguintes packages e as suas
versões correspondentes:
- lxml==4.0.0
- Wikidata==0.6.1
- s4api==1.1.0
- requests==2.18.4

Para executar a aplicação, é necessário executar o servidor GraphDB,
depois deve abrir a pasta do projeto (Projeto2) e executar o seguinte comando:
python3 manage.py runserver (ou simplesmente fazer Run do projeto
caso utilize o PyCharm). A aplicação fica acessível no browser via URL
127.0.0.1:8000 (equivalente a localhost:8000).

Se não existirem as bases de dados necessárias para a aplicação, serão
automaticamente criadas e preenchidas com os dados presentes nos ficheiros
de backup.

Existe inicialmente um utilizador registado na plataforma, mas podem
ser adicionados mais utilizadores. Os tuplos (username, password) dos utilizadores
atuais são (admin, rootroot).