🐘 Memória de Elefante
Um jogo da memória interativo desenvolvido com CustomTkinter, oferecendo múltiplos temas visuais para testar e aprimorar sua memória!

📋 Visão Geral
O Memória de Elefante é um jogo clássico de memória onde o jogador deve encontrar pares de cartões idênticos. O jogo oferece 5 temas diferentes para manter a diversão sempre variada e desafiadora.

🎯 Características
5 Temas Exclusivos:

🎨 Cores

🐾 Animais

🌸 Flores

🚗 Carros

🏁 Bandeiras

Sistema de Pontuação: Limite de 25 tentativas para completar todos os 8 pares

Interface Moderna: Design escuro com elementos visuais atraentes

Múltiplos Jogos Independentes: Cada tema mantém seu próprio progresso

Feedback Visual: Efeitos de animação para pares encontrados

Menus Informativos: Sobre o jogo e informações dos desenvolvedores

📦 Pré-requisitos
Python 3.7 ou superior

Pip (gerenciador de pacotes Python)

🔧 Instalação
Passo 1: Clone o repositório
```bash
git clone https://github.com/seu-usuario/memoria-de-elefante.git
cd memoria-de-elefante
```
Passo 2: Instale as dependências
```bash
pip install customtkinter Pillow
```
Passo 3: Estrutura de Diretórios
Certifique-se de que a estrutura de diretórios esteja correta:

```text
memoria-de-elefante/
├── img/
│   ├── menu.png
│   ├── black.png
│   ├── animais/
│   │   ├── img1.jpg
│   │   ├── img2.jpg
│   │   ├── ...
│   ├── flores/
│   │   ├── img1.jpg
│   │   ├── img2.jpg
│   │   ├── ...
│   ├── carros/
│   │   ├── img1.jpg
│   │   ├── img2.jpg
│   │   ├── ...
│   └── bandeiras/
│       ├── img1.jpg
│       ├── img2.jpg
│       ├── ...
├── main.py
├── LICENSE
└── README.md
```

🚀 Como Jogar
Execute o jogo:
```
python main.py
```
Selecione um tema: Clique nas abas para escolher entre Cores, Animais, Flores, Carros ou Bandeiras

Clique nos cartões: Vire os cartões para encontrar os pares correspondentes

Acompanhe seu progresso: Veja suas tentativas e pares encontrados na parte inferior

Reinicie quando quiser: Use o botão "Reiniciar Jogo" para um novo desafio

🎮 Regras do Jogo
Encontre todos os 8 pares de cartões

Você tem 25 tentativas para completar o jogo

Ao encontrar um par, os cartões são eliminados com um efeito verde ✓

Cartões diferentes são virados novamente após 1 segundo

O jogo termina quando você encontra todos os pares ou esgota as tentativas

🛠️ Tecnologias Utilizadas
CustomTkinter: Interface gráfica moderna e responsiva

PIL (Pillow): Manipulação e exibição de imagens

Random: Embaralhamento aleatório dos cartões

OS/Pathlib: Gerenciamento de arquivos e diretórios

📱 Funcionalidades Especiais
Sistema Multi-temas
Cada tema opera de forma independente, permitindo que você jogue diferentes temas sem perder o progresso de cada um.

Gerenciamento de Imagens
O jogo tenta carregar imagens de dois locais diferentes, garantindo compatibilidade mesmo em ambientes com restrições de permissão.

Interface Adaptativa
Design responsivo que se adapta a diferentes tamanhos de tela com tamanhos de cartão otimizados.

🐛 Solução de Problemas
Imagens não aparecem
Verifique se a pasta img está no mesmo diretório do script e contém todas as subpastas com as imagens necessárias.

Erro ao importar CustomTkinter
bash
pip install --upgrade customtkinter
Erro de permissão no Linux
O jogo tenta criar automaticamente a pasta .MemoriaDeElefante no diretório home do usuário para armazenar imagens.

🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para:

Reportar bugs

Sugerir novos temas

Melhorar a interface

Adicionar novas funcionalidades

Como contribuir:
Faça um fork do projeto

Crie sua branch de feature (git checkout -b feature/AmazingFeature)

Commit suas mudanças (git commit -m 'Add some AmazingFeature')

Push para a branch (git push origin feature/AmazingFeature)

Abra um Pull Request

👨‍💻 Desenvolvedores
Autor Principal
João Salvador Paulo

Desenvolvimento e Design

Contato: +244 949 160 426

Jeel Devs
Projeto desenvolvido pela Jeel Devs - criando experiências interativas inovadoras.

📄 Licença
Este projeto está sob a licença GNU General Public License v3.0 - veja o arquivo LICENSE para mais detalhes.

Resumo da Licença GPLv3:
✅ Você pode usar, modificar e distribuir este software

✅ Você pode usar este software para fins comerciais

⚠️ Você deve manter o aviso de copyright e licença

⚠️ Você deve disponibilizar o código fonte de quaisquer modificações

⚠️ Você deve distribuir suas modificações sob a mesma licença GPLv3

❌ Você não pode impor restrições adicionais aos usuários

Arquivo LICENSE
Crie um arquivo LICENSE no diretório do projeto com o seguinte conteúdo:


🎯 Próximos Passos
Adicionar mais temas (Comidas, Esportes, etc.)

Sistema de recordes e pontuação

Modo multiplayer local

Efeitos sonoros

Níveis de dificuldade

Salvar progresso entre sessões

📊 Estatísticas do Projeto
Linhas de Código: ~800

Temas Disponíveis: 5

Total de Imagens: 40+

Tempo de Desenvolvimento: 2 semanas

🙏 Agradecimentos
CustomTkinter pela excelente biblioteca de interface

Pillow pelo suporte a imagens

Comunidade open-source por todo o suporte

⭐ Se você gostou do projeto, não esqueça de dar uma estrela no GitHub! ⭐

Desenvolvido com ❤️ por João Salvador Paulo e Jeel Devs

"A memória é o diário que todos carregamos conosco." - Oscar Wilde
