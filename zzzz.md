1 - Crie o ambiente virtual para o projeto
python3 -m venv .venv && source .venv/bin/activate
2 - Instale as dependências
python3 -m pip install -r dev-requirements.txt
3 - Para garantir a qualidade do código, vamos utilizar neste projeto o linter Flake8
$ python3 -m flake8

Ambiente Virtual
1 - criar o ambiente virtual
$ python3 -m venv .venv
2 - ativar o ambiente virtual
$ source .venv/bin/activate
3 - instalar as dependências no ambiente virtual
$ python3 -m pip install -r dev-requirements.txt

Executar os Testes
1 - todos testes
$ python3 -m pytest
2 - Caso precise executar apenas uma função de testes basta executar o comando:
$ python3 -m pytest -k nome_da_func_de_tests
3 - Para executar um teste específico de um arquivo, basta executar o comando:
$ python -m pytest -x tests/nome_do_arquivo.py::test_nome_do_teste

Requisitos
2 - pytest.raises
https://docs.pytest.org/en/7.1.x/how-to/assert.html
3 - exemplos de resoluçao
https://stackoverflow.com/questions/952110/recursive-function-palindrome-in-python
4-
https://www.alura.com.br/artigos/algoritmo-quicksort-implementar-python?gclid=CjwKCAiAmuKbBhA2EiwAxQnt7-Zn7sfECko-5NfrdvBGyEzkGiJ2LBu312TFLMKvue-dYVqsFhBBAxoChg4QAvD_BwE
https://wiki.python.org.br/QuickSort
