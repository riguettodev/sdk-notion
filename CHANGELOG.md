# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [Unreleased]

## [0.1.0-beta] - 2026-01-23

### Added

- Sistema de autenticação com suporte a múltiplas versões da API (`legacy` e `data_sources`)
- Client HTTP para endpoints `pages`, `databases` e `blocks`
- Sistema ORM declarativo com `NotionDatabase` para mapeamento de schemas
- Registry global de databases com `DatabaseRegistry`
- Container pattern para organização de databases (`DatabasesContainer`)
- Repositories para `pages` e `databases` com fluent interface
- Query builders (`QueryFilter` e `QuerySort`)
- Property extractors e parsers automáticos
- Schemas Pydantic para todas as respostas da API
- Suporte a Generic Types para autocomplete perfeito
- Computed fields e validators customizados
- Configuração global de timezone via `ORMConfig`
- Singleton pattern para Client configurável
- Transformers customizáveis para processamento de propriedades

### Notes

- Primeira release beta do projeto
- Documentação completa em desenvolvimento
- Alguns tipos de propriedades ainda não suportados

[0.1.0-beta]: [https://github.com/riguettodev/sdk-notion/releases/tag/v0.1.0-beta](https://github.com/riguettodev/sdk-notion/releases/tag/v0.1.0-beta)
