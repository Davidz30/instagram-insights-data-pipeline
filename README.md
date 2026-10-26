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

**O repositório deve permanecer privado até a revisão final.** Confirme permissões de uso
do código, ausência de segredos em todo o histórico e resultados do GitHub Actions.
Consulte [SECURITY.md](SECURITY.md).

Este código é uma **implementação demonstrativa adaptada**, não uma cópia dos scripts
de produção. A compatibilidade operacional e os resultados de métricas precisam
ser validados em um ambiente de testes antes de qualquer uso real.
