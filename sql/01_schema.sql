-- Generic demonstration schema. No real account identifiers or credentials.
CREATE TABLE dbo.d_instagram_contas (
    INSTAGRAM_ID varchar(30) NOT NULL PRIMARY KEY,
    ATIVO bit NOT NULL DEFAULT 1,
    DTA_CADASTRO datetime2 NOT NULL DEFAULT SYSUTCDATETIME()
);
GO
CREATE TABLE dbo.f_instagram_midias (
    MEDIA_ID varchar(30) NOT NULL,
    INSTAGRAM_ID varchar(30) NOT NULL,
    DTA_PUBLICACAO datetime2 NOT NULL,
    MEDIA_TYPE varchar(30) NULL,
    MEDIA_PRODUCT_TYPE varchar(30) NULL,
    LIKE_COUNT int NULL,
    COMMENTS_COUNT int NULL,
    REACH int NULL,
    SAVED int NULL,
    SHARES int NULL,
    TOTAL_INTERACTIONS int NULL,
    DTA_CARGA datetime2 NOT NULL DEFAULT SYSUTCDATETIME(),
    CONSTRAINT PK_instagram_midias PRIMARY KEY (MEDIA_ID, INSTAGRAM_ID)
);
GO
CREATE TABLE dbo.f_instagram_insights_conta (
    ID bigint IDENTITY(1,1) NOT NULL PRIMARY KEY,
    INSTAGRAM_ID varchar(30) NOT NULL,
    DTA_INICIO date NOT NULL,
    DTA_FIM date NOT NULL,
    FOLLOWERS_COUNT int NULL,
    MEDIA_COUNT int NULL,
    REACH int NULL,
    PROFILE_VIEWS int NULL,
    ACCOUNTS_ENGAGED int NULL,
    DTA_CARGA datetime2 NOT NULL DEFAULT SYSUTCDATETIME(),
    CONSTRAINT UQ_instagram_insights_conta UNIQUE (INSTAGRAM_ID, DTA_INICIO, DTA_FIM)
);
GO
