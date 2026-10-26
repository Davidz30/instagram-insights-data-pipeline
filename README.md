# Instagram Insights Data Pipeline

Pipeline demonstrativo independente: **Instagram Graph API → Python → SQL Server → Power BI**.

## Conteúdo

- `src/carga_instagram_midias.py`: metadados de mídias e indicadores de engajamento.
- `src/carga_insights_conta.py`: métricas diárias por conta.
- `src/common.py`: configuração externa, cliente da API e conexão SQL.
- `sql/`: tabelas e views genéricas de demonstração.
- `docs/`: arquitetura, instalação, operação e privacidade.
- `.github/workflows/security.yml`: verificações de segurança.
- `examples/`: dados inteiramente fictícios.

## Como executar

Consulte [docs/SETUP.md](docs/SETUP.md). Configure as credenciais fora do repositório.
O projeto não inclui contas, infraestrutura ou credenciais reais.

## Segurança e publicação

O projeto foi preparado para exibição em portfólio. Foram executadas verificações automatizadas de sintaxe, testes unitários, dependências, análise estática e detecção de segredos, além de uma varredura do histórico Git. Esses controles não garantem ausência de falhas ou dados sensíveis. Consulte [SECURITY.md](SECURITY.md).

Este código é uma **implementação demonstrativa adaptada**, não uma cópia dos scripts
de produção. A compatibilidade operacional e os resultados de métricas precisam
ser validados em um ambiente de testes antes de qualquer uso real.

## Licença e direitos de uso

**Todos os direitos reservados.** Este repositório é disponibilizado exclusivamente para consulta e demonstração de portfólio. Nenhuma licença de uso, cópia, modificação, distribuição ou exploração comercial do código é concedida. A disponibilidade pública no GitHub não implica autorização para reutilização.

## Limitações da demonstração

O modelo original foi testado pelo autor em produção, mas esta versão demonstrativa independente **não foi submetida a testes funcionais de integração** com a API Meta e o SQL Server. Não deve ser considerada pronta para produção.
