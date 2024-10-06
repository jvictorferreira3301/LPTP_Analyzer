# Análise Estatística da Sincronização de Tempo em Redes Locais Usando LinuxPTP ⏰

Este repositório contém um notebook Jupyter que realiza uma análise estatística da sincronização de tempo em redes locais utilizando o LinuxPTP. Este trabalho foi desenvolvido como parte da disciplina EC01019 - PROBABILIDADE E ESTATISTICA ministrada no quarto semestre da [Faculdade de Engenharia da Computação e Telecomunicações](https://www.itec.ufpa.br/index.php?option=com_content&view=article&id=211:faculdade-de-engenharia-da-computacao-e-telecomunicacoes&catid=74&Itemid=114&lang=pt) da [Universidade Federal do Pará](https://ufpa.br/).

## Descrição 📖

A sincronização precisa de tempo em redes de computadores é fundamental para diversas aplicações, incluindo redes industriais, telecomunicações e data centers. Neste trabalho, utilizamos o [LinuxPTP](https://linuxptp.sourceforge.net/), uma implementação do [**Precision Time Protocol (PTP)**](https://endruntechnologies.com/pdf/PTP-1588.pdf), para simular e analisar a sincronização de tempo entre diferentes nós de uma rede.

A análise deste trabalho é feita utilizando **Estatística Descritiva e Inferencial**, com a aplicação de **testes de hipóteses** para avaliar o comportamento da sincronização em diferentes cenários. Para isso, configuramos nós em uma rede local que atuam como mestres e escravos PTP, e coletamos dados de _**Time offset**_ durante a sincronização.

## Objetivos ✅

Os principais objetivos deste trabalho incluem:

- **Testar Timestamping em Software vs. Hardware**: Comparar a eficácia da sincronização utilizando **timestamping em software** e **timestamping em hardware**.
- **Avaliar a Qualidade da Sincronização**: Examinar se o **offset** entre o mestre e o escravo se mantém próximo de zero em diferentes condições de rede.
- **Comparar Topologias de Sincronização**: Verificar a eficácia de diferentes configurações, como topologias **mestre-escravo** simples e aquelas que envolvem **_Transparent Clocks_** ou **_Boundary Clocks_**.

## Ambiente de Testes 💻

Para este estudo, utilizamos 3 computadores cujas especificações são descritas na tabela abaixo:

| Especificação      | PC 1                | PC 2                | PC 3                     |
|--------------------|------------------------------|----------------------------------|--------------------------------------|
| OS                 | Ubuntu 22.04.5 LTS           | Ubuntu 22.04.4 LTS               | Ubuntu 18.04.4 LTS                   |
| Kernel             | 6.8.0-45-generic             | 6.5.0-35-generic                 | 4.15.0-213-generic                   |
| NIC                | Intel X550-T2 PCI-E X4       | Intel X550-T2 PCI-E X4           | Intel X550-T2 PCI-E X4               |
| CPU                | Intel i5-7600 (4) 4.1GHz     | Intel i5-9400 (6) 4.1GHz         | Intel i7-5930K (12) 3.7GHz           |
| GPU                | Intel HD Graphics 630        | Intel HD Graphics 630            | AMD Radeon HD 7770/8760              |
| Memory             | 8GB                          | 16GB                             | 64GB                                 |

**Tabela 1** - Especificações dos computadores utilizados nos testes.

Os dados são coletados diretamente dos logs do **ptp4l**, a ferramenta do LinuxPTP que executa a sincronização.

## Estrutura do Repositório  📁

```plaintext
LPTP_Analyzer/
├── LPTP_Analyzer.ipynb       # Notebook Jupyter contendo a análise completa
├── logs/                     # Diretório contendo os arquivos de log utilizados na análise
│   ├── Hard.txt
│   ├── Soft.txt
│   └── ...
├── assets/                   # Diretório contendo as imagens utilizadas no notebook
│   ├── topo1.png
│   ├── topo2.png
│   └── ...
├── log_processing.py         # Script Python para processar os logs do ptp4l
├── plotting.py               # Script Python para gerar os gráficos da análise
└── requirements.txt         
```
## Como Executar 🔨

1. Clone o repositório:
    ```bash
    git clone https://github.com/jvictorferreira3301/LPTP_Analyzer
    cd LPTP_Analyzer
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Abra o notebook Jupyter, ou abra pelo badge no colab ou visualize localmente com VS code:
    ```bash
    jupyter notebook LPTP_Analyzer.ipynb
    ```

4. Execute as células do notebook para reproduzir a análise.

## Referências 📚

- [LinuxPTP](https://linuxptp.sourceforge.net/)
- [Precision Time Protocol (PTP)](https://endruntechnologies.com/pdf/PTP-1588.pdf)
- [Cisco PTP Guide](https://www.cisco.com/c/en/us/td/docs/dcn/aci/apic/5x/system-management-configuration/cisco-apic-system-management-configuration-guide-51x/m-precision-time-protocol.html)

## Licença 📄

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
