import random
import string

def generate_strong_password(length=16):
    uppercase = random.sample(string.ascii_uppercase, 2)
    lowercase = random.sample(string.ascii_lowercase, 4)
    numbers = random.sample(string.digits, 4)
    symbols = random.sample('!@#$%^&*', 2)
    core = uppercase + lowercase + numbers + symbols
    middle_padding = length - 6 - len(core)
    extra = random.choices(string.ascii_letters + string.digits + '!@#$%^&*', k=middle_padding)
    full_password = core + extra
    random.shuffle(full_password)
    final = ''.join(full_password) + 'x' * 6
    return final

if __name__ == '__main__':
    print("Generated Strong Password:", generate_strong_password())
