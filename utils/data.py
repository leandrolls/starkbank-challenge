import random


def gen_random_value():
    random_value = random.randint(1000, 1000000)
    return random_value


def gen_random_name():
    names_list = ['Miguel', 'Arthur', 'Heitor', 'Adriana', 'Ana', 'Maria', 'Sandra', 'Juliana', 'Helena', 'Madalena',
                  'Antônio', 'Carlos', 'Francisco', 'João', 'José', 'Afonso', 'Lourenço', 'Bruna','Camila','Jéssica',
                  'Letícia', 'Amanda', 'Betina','Lucas', 'Luís', 'Mateus', 'Guilherme', 'Pedro','Heloísa', 'Maria Clara',
                  'Maria Cecília', 'Maria Júlia','Maitê', 'Maria Eduarda', 'Elisa', 'Samuel', 'Benício']
    random_name = random.choice(names_list)
    return random_name


def gen_random_lastname():
    lastname_list = ['Silva', 'Souza', 'Lima', 'Santos', 'Ferreira', 'Bittencourt', 'Oliveira', 'Rodrigues', 'Alves',
                        'Pereira', 'Gomes', 'Ribeiro', 'Martins', 'Andrade', 'Barbosa', 'Barros', 'Campos', 'Lopes',
                        'Machado']
    random_lastname = random.choice(lastname_list)
    return random_lastname
