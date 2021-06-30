# automation-tools

**encrypt_var_string.py**

Encrypting multiple ansible variables using automation in one go. 

-- This also help if you are using Ansible Tower as variable need to be vault string encrypted instead of encrypting complete vault file to avoid dynamic inventory loading issue with ansible tower. 

-- with complete encrypted vault file content you always have to decrypt the vaulted file to see which variables are there. So it is better to encrypt each variable as vaulted string variable as those will be easy to search and helps in debug

How to use :
1) export vault credentials
export ANSIBLE_VAULT_PASSWORD_FILE=/home/sm/v.txt
v.txt — plain text file containing vault password
2) run script
python encrypt_var_string.py test.yml > output.yml
test.yml — input file having list of variables to encrypt
output.yml — output file generated with vaulted string variables.

Sample input file :

[smhatre@at ~]$ cat test.yml

test: “bdasbdk$asd kjasdkjasd”

test_key: |
MIIEogIBAAKCAQEAoanA/Ohcw5HiEN2Mmzs/RBImxgiW6J7dBVp+76673McaUj8R

Sample output file :

this is how sample output file get created by script

[smhatre@at ~]$ cat output.yml (trimmed output)

test: !vault |
$ANSIBLE_VAULT;1.1;AES256
37396666346165323136316133616337626434643733393065646366363134376635666432633838
3531633663326239316332326635616637316162316165660a376438616166346261643763666331

test_key: !vault |
$ANSIBLE_VAULT;1.1;AES256
35396331393138373930646134316639323837646538306663393862336562313964383662336537
3562386137343731663339373933353534643330356133390a333366356537636466633537656135

Tips:

you can always ensure/verify correct vault value by using below ansible command.

ansible localhost -m ansible.builtin.debug -a var=”test” -e “@output.yml” — ask-vault-pass
this will print variable value.

