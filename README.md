# kzs-json-subl

- Extrai json com base no que esta selecionado, ou se não tiver nada selecionado no arquivo todo
- Se for um objeto, se baseia no primeiro `{` e no ultimo `}` para definir o inicio e final do json
- Se for um array, se baseia no primeiro `[` e no ultimo `]` para definir o inicio e final do json
- Substitui os `\"\"` por `""`
- Substitui os `\"` por `"`
- Remove os `\n`
- Formata o json com base na lib json do python, usando a config de 4 espaços
- Se o json não for válido mostra um popup de error dentro do proprio sublime
- Se o json for valido substitui o texto selecionado, ou se não tiver selecionado, substitui o arquivo inteiro, pelo json formatado

## Add extension to config

- Adicione o arquivo [kzsjsonsubl.py](https://github.com/kielsonzinn/kzs-json-subl/blob/main/kzsjsonsubl.py) ao diretorio de configs do sublime-text
- O diretorio de config do subl-text geralmente é `~/.config/sublime-text/Packages/User`
  
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
