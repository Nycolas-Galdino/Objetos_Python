# Biblioteca de módulos individuais em Python 🐍

Como todos sabem, bons desenvolvedores não escondem seus segredos. Deixei aqui públicado meus objetos pessoais em Python, eles são excelentes para agilizar atualizar seus projetos! 👨‍💻

> **NOTA:** Os códigos foram testados apenas no windows, não sei como estarão funcionando em outros SO como Linux e Mac.
# Quais módulos irei encontrar aqui?

Você poderá encontrar os seguintes módulos:

## Automação Gui
<details>
    O objeto <code>Obj_Automation_GUI.py</code> foi criado para automações GUI em python utilizando reconhecimento por imagem para realizar suas ações. Pode lhe ser útil algum dia!
</details>

## Azure Functions
<details>
    O objeto <code>Obj_Azure_Functions.py</code> foi criado para mexer diretamente em seu serviço Azure usando o método ConnectionString como base.
</details>

## Databases
<details>
    O objeto <code>Obj_Databases.py</code> foi criado para mexer diretamente em um banco SQLite sem nenhum problema, recomendado para projetos de pequeno/médio porte.
</details>

## Email
<details>
    O objeto <code>Obj_EmailSender.py</code> foi criado para enviar e-mails de forma dinâmica sem muitos problemas ou configurações.
</details>

## PDF Reader
<details>
    O objeto <code>Obj_PDF_Reader.py</code> foi criado para ler PDF's de maneira dinâmica usando PyMuPDF (fitz) ou PDFReader, depende de sua escolha.
</details>

## Read Settings
<details>
    O objeto <code>Obj_Read_Settings.py</code> foi criado para ler configurações em arquivos YAML, porém, por ser um arquivo bem curto acaba sendo simples sua adaptação.
</details>

## Requests
<details>
    O objeto <code>Obj_Requests.py</code> foi criado para fazer requests igualmente à biblioteca `requests` do python, porém, com o diferencial de ser um app que valida se o request foi realizado com sucesso ou não, e dependendo do caso converte a resposta em json para você.
</details>

## Web Automation
<details>
    O objeto <code>Obj_WebAutomation.py</code> foi criado para automatizar sua busca em sites de maneira bem dinâmica, contendo diversas funcionalidades que podem lhe ajudar e muito em seu processo de automação.
</details><br>

# Como usar esses módulos?

Para usar esses módulos, você precisará seguir algumas etapas:

## 1. Clone este repositório para o seu computador:

```bash
git clone https://github.com/Nycolas-Galdino/Objetos_Python.git
```

## 2. Navegue até o diretório do repositório:

```cmd
cd Objetos_Python
```

## 3. Acesse a pasta `Objetos`

```cmd
cd Objetos
```

## 4. Selecione o/os objeto(s) que deseja copiar e cole diretamente em seu projeto Python

Por exemplo: caso queira copiar o objeto de ler configurações, pode utilizar o comando:

```cmd
copy Obj_Read_Settings.py <caminho_do_seu_projeto_aqui>
```

## 5. Instale as bibliotecas necessárias

Acesse o objeto que deseja e veja quais módulos ele possui instalado, por exemplo: para o objeto Obj_Read_Settings.py (que lê as configurações de arquivos yaml), ele utiliza o módulo yaml, e você pode instalar ele utilizando o comando:

```cmd
python -m pip install python-yaml
```

# Contribua

> **Se você deseja contribuir para este projeto, sinta-se à vontade para abrir uma solicitação de pull ou enviar um problema. Estou aberto a sugestões e melhorias!**