# Novo Projeto - FlashWhats

Este projeto é uma aplicação chamada **FlashWhats**, que permite o envio automático de mensagens via WhatsApp utilizando a biblioteca `pywhatkit`. A aplicação possui uma interface gráfica construída com `Tkinter`, onde o usuário pode inserir uma lista de contatos e uma mensagem personalizada.

## Estrutura do Projeto

O projeto contém os seguintes arquivos:

- **app.py**: Contém a lógica principal da aplicação, incluindo a interface gráfica, funções para extrair contatos e enviar mensagens via WhatsApp.
- **requirements.txt**: Lista as dependências necessárias para o funcionamento da aplicação.
- **README.md**: Documentação do projeto, incluindo instruções de configuração e execução.

## Instalação

Para configurar e executar a aplicação, siga os passos abaixo:

1. **Clone o repositório** ou **baixe os arquivos** do projeto.
2. **Instale as dependências** necessárias. Execute o seguinte comando no terminal:

   ```
   pip install -r requirements.txt
   ```

3. **Execute a aplicação**. Após instalar as dependências, inicie a aplicação com o comando:

   ```
   python app.py
   ```

## Uso

1. Insira a lista de contatos no formato `Nome(DDD)Número` na área designada.
2. Escreva a mensagem que deseja enviar, utilizando `{nome}` para personalizar a mensagem com o nome do contato.
3. Clique no botão "Enviar Mensagens" para iniciar o envio.
4. Para interromper o envio, clique no botão "Parar Envio".

## Observações

- Certifique-se de que o WhatsApp Web esteja aberto na primeira aba do seu navegador antes de iniciar o envio das mensagens.
- O envio de mensagens pode levar algum tempo, dependendo do número de contatos.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções. Para isso, faça um fork do repositório e envie suas alterações.
