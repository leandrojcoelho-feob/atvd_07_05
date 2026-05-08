# Sistema de Gestão de Cinemas

## Regras de Negócio Essenciais
* **RN01 (Capacidade Máxima):** O público registrado em uma sessão jamais pode ultrapassar a capacidade máxima estipulada para o cinema onde a sessão ocorre. O sistema deve bloquear a operação caso isso ocorra.
* **RN02 (Privilégios de Acesso - RBAC):** Operações de escrita e alteração no banco de dados (cadastros e registros) são estritamente exclusivas do perfil "Funcionário". O perfil "Público" possui apenas permissão de leitura.
* **RN03 (Integridade de Dados):** O sistema não deve permitir o cadastro de durações ou capacidades com valores negativos ou iguais a zero. Entradas que exigem números (IDs, capacidade, duração) devem ser validadas para evitar falhas caso o usuário digite texto.
