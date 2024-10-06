# kzs-json-subl

- Extrai json com base no que esta selecionado, ou se não tiver nada selecionado no arquivo todo
- Se baseia no primeiro `{` e no ultimo `}` para definir o inicio e final do json
- Substitui os `\"\"` por `""`
- Substitui os `\"` por `"`
- Remove os `\n`
- Formata o json com base na liv json do python, usando a config de 4 espaços
- Se o json não for válido mostra um popup de error dentro do proprio sublime
- Se o json for valido mostra um popup com o json formatado, pedindo confirmação
- Caso confirmado substitui o texto selecionado, ou se não tiver selecionado, substitui o arquivo inteiro, pelo json formatado

## Add on keymap

- Preferences
    - Key Bindings
```json
[
    {
        "keys": ["ctrl+shift+alt+f"],
        "command": "kzsjsonsubl"
    }
]
```
