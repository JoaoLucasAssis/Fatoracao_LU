# Resolução de Sistemas de Equações Lineares com Fatoração LU

Este projeto implementa um algoritmo em Python para resolver sistemas de equações lineares com n variáveis usando o método de Fatoração LU.

A fatoração LU decompõe a matriz de coeficientes em duas matrizes triangulares: uma matriz triangular inferior (L) e uma matriz triangular superior (U).

Este algoritmo implementa as substituições progressivas(Ly = b) e regressivas(Ux = y) para resolver o sistema de equações.

Para executar o algoritmo, os arquivos `matrix.txt` e `b.txt` podem ser modificados conforme necessário para representar o sistema de equações desejado.

> :warning: obs: Certifique-se de que o arquivo segue o formato estabelecido no tópico de execução.

## Instalação
<details>
<summary>Clique aqui!</summary>
<p>

### Pré-requisitos para instalação!

![Git](https://img.shields.io/badge/Git-E34F26?style=for-the-badge&logo=git&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
--------------------------------------------------------------------------------------------

Para começar, clone o repositório do projeto em seu ambiente local. Siga a etapa abaixo:

* Abra o terminal na pasta onde deseja clonar o repositório.

* Clone o repositório para o seu ambiente local usando o seguinte comando:

```git
git clone https://github.com/JoaoLucasAssis/Git_Workflow.git
```

> :warning: obs: Certifique-se de ter o git instalado antes de executar o comando no terminal

* Navegue até o diretório onde o repositório foi baixado:

```git
cd sorting-algorithms-comparison
```

* Adicione em `matrix.txt` a matriz que você deseja decompor.

> :warning: obs: Certifique-se de que o arquivo segue o formato estabelecido no tópico de execução.

* Execute o script python:

```python
python .\src\main.py
```

</p>
</details>

## Dependências

Este projeto não possui dependências externas além das bibliotecas padrão do Python.

## Ambiente de Desenvolvimento e Execução

O algoritmo foi desenvolvido no ambiente do Visual Studio Code (VSCode). 

Foi utilizado um interpretador Python e um ambiente virtual(venv) para gerenciar as dependências e isolar o ambiente de desenvolvimento.

**O arquivo contendo a matriz do sistema de equações deve seguir o seguinte formato:**

* Cada linha representa uma equação do sistema.

* Os coeficientes das variáveis devem estar separados por espaços.
 
**O arquivo contendo o vetor de termos independentes deve seguir o seguinte formato:**

* Cada linha representa o termo independente correspondente à equação.

Esta é a estrutura do projeto FATORACAO_LU:

```
/FATORACAO_LU
├── /.venv
├── /src
│   ├── main.py
│   └── /scripts
│       ├── /__pycache__
│       ├── lu_decomposition.py
│       └── substitution.py
├── matrix.txt
├── b.txt
└── README.md
```

## Colaboradores

<table>
  <tr>
  <!-- João Lucas -->
    <td align="center">
      <a href="https://github.com/JoaoLucasAssis">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwxCRWlkfeigdbif83ap111RPNlGARl02wOF5OvW9zUA&s" width="100px;" height="100px;" alt="Foto do João Lucas"/><br>
        <sub>
          <b>JoaoLucasAssis</b>
        </sub>
      </a>
    </td>
        <!-- Vitor Lugon -->
    <td align="center">
      <a href="https://github.com/VitorLugon">
        <img src="https://i.pinimg.com/originals/e5/df/45/e5df457e8de5d0aae37691c00e8a672e.jpg" width="100px;" height="100px;" alt="Foto do Vitor Lugon"/><br>
        <sub>
          <b>VitorLugon</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

## Licença

Este projeto é distribuído sob a Licença MIT. Sinta-se à vontade para usar, modificar e distribuir este código conforme necessário.